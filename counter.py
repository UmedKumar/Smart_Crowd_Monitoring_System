import cv2
import numpy as np
import os
import datetime
from ultralytics import YOLO
from deepface import DeepFace
import winsound

# --- CONFIGURATION & TUNING CONSTANTS ---
# -- Sneaking Detection --
SNEAKING_ASPECT_RATIO_THRESHOLD = 1.8
SNEAKING_SPEED_THRESHOLD = 25
SNEAKING_CONFIDENCE_FRAMES = 15

# -- Hiding/Loitering Detection --
LOITERING_SPEED_THRESHOLD = 10
LOITERING_CONFIDENCE_FRAMES = 80

# --- SETUP DIRECTORIES ---
KNOWN_FACES_DIR = "known_faces"
ALERT_DIR = "alert_captures"
if not os.path.exists(KNOWN_FACES_DIR): os.makedirs(KNOWN_FACES_DIR)
if not os.path.exists(ALERT_DIR): os.makedirs(ALERT_DIR)

# --- MODEL & WEBCAM SETUP ---
# Upgraded to 'yolov8m.pt' (medium model) for higher accuracy.
model = YOLO('yolov8m.pt') 
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# --- FACE RECOGNITION SETUP ---
known_face_embeddings, known_face_ids = [], []
print("Loading known faces...")
for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.endswith((".jpg", ".png")):
        face_id = os.path.splitext(filename)[0]
        image_path = os.path.join(KNOWN_FACES_DIR, filename)
        img = cv2.imread(image_path)
        if img is not None:
            try:
                embedding_obj = DeepFace.represent(img, model_name='VGG-Face', enforce_detection=False)
                embedding = embedding_obj[0]["embedding"]
                known_face_embeddings.append(np.array(embedding))
                known_face_ids.append(face_id)
            except Exception as e:
                print(f"Could not process image {filename}: {e}")
print(f"Loaded {len(known_face_ids)} known faces.")

# --- INITIALIZE TRACKING DICTIONARIES AND COUNTERS ---
next_person_id = len(known_face_ids) + 1
track_id_to_face_id, track_positions, track_history = {}, {}, {}
sneaking_tracker, loitering_tracker, alert_triggered = {}, {}, {}
people_in, people_out, alert_count = 0, 0, 0

# --- SETUP FULL-SCREEN WINDOW ---
WINDOW_NAME = "Advanced Security Monitor"
cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# --- MAIN PROCESSING LOOP ---
while True:
    ret, frame = cap.read()
    if not ret: break

    height, width, _ = frame.shape
    line_x = width // 2
    
    results = model.track(frame, persist=True, verbose=False) 
    annotated_frame = results[0].plot()
    cv2.line(annotated_frame, (line_x, 0), (line_x, height), (0, 255, 255), 2)

    if results[0].boxes.id is not None:
        track_ids = results[0].boxes.id.int().cpu().tolist()
        boxes = results[0].boxes.xyxy.cpu()
        class_ids = results[0].boxes.cls.int().cpu().tolist()

        for track_id, box, class_id in zip(track_ids, boxes, class_ids):
            if model.names[class_id] == 'person':
                x1, y1, x2, y2 = map(int, box)
                center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
                
                # --- BEHAVIOR ANALYSIS ---
                speed = 0
                if track_id in track_history:
                    last_x, last_y = track_history[track_id]
                    speed = np.sqrt((center_x - last_x)**2 + (center_y - last_y)**2)
                track_history[track_id] = (center_x, center_y)

                box_w, box_h = x2 - x1, y2 - y1
                aspect_ratio = box_h / box_w if box_w > 0 else 0
                
                is_sneaking = aspect_ratio < SNEAKING_ASPECT_RATIO_THRESHOLD and speed < SNEAKING_SPEED_THRESHOLD
                if is_sneaking: sneaking_tracker[track_id] = sneaking_tracker.get(track_id, 0) + 1
                else: sneaking_tracker[track_id] = 0

                is_loitering = speed < LOITERING_SPEED_THRESHOLD
                if is_loitering: loitering_tracker[track_id] = loitering_tracker.get(track_id, 0) + 1
                else: loitering_tracker[track_id] = 0
                
                if not is_sneaking and not is_loitering:
                    alert_triggered[track_id] = False

                # --- ALERT TRIGGER ---
                alert_reason = None
                if sneaking_tracker.get(track_id, 0) >= SNEAKING_CONFIDENCE_FRAMES:
                    alert_reason = "SNEAKING"
                elif loitering_tracker.get(track_id, 0) >= LOITERING_CONFIDENCE_FRAMES:
                    alert_reason = "LOITERING"

                if alert_reason:
                    if not alert_triggered.get(track_id, False):
                        # *** SMART BEEP LOGIC ***
                        # Only beep if the person is sneaking AND their face is not recognized.
                        is_unidentified = track_id not in track_id_to_face_id
                        if alert_reason == "SNEAKING" and is_unidentified:
                            winsound.Beep(3000, 700) # Higher pitch, longer duration for critical alert
                        
                        alert_triggered[track_id] = True
                        alert_count += 1
                        
                        # Save a picture of any unidentified person during any alert
                        if is_unidentified:
                            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                            filename = f"alert_{alert_reason.lower()}_{track_id}_{timestamp}.jpg"
                            person_crop = frame[y1:y2, x1:x2]
                            cv2.imwrite(os.path.join(ALERT_DIR, filename), person_crop)
                    
                    cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 0, 255), 4)
                    cv2.putText(annotated_frame, f"ALERT: {alert_reason}!", (x1, y1 - 30), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 255), 2)
                
                # --- Standard Counting and Face ID Logic ---
                current_pos = 1 if center_x > line_x else -1
                if track_id not in track_id_to_face_id:
                    person_crop = frame[y1:y2, x1:x2]
                    if person_crop.size > 0:
                        try:
                            embedding_obj = DeepFace.represent(person_crop, model_name='VGG-Face', enforce_detection=True)
                            embedding = np.array(embedding_obj[0]["embedding"])
                            face_id = "Unknown"
                            if len(known_face_embeddings) > 0:
                                distances = np.linalg.norm(np.array(known_face_embeddings) - embedding, axis=1)
                                min_dist_idx = np.argmin(distances)
                                if distances[min_dist_idx] < 0.4: face_id = known_face_ids[min_dist_idx]
                            
                            if face_id == "Unknown":
                                face_id = f"Person {next_person_id}"
                                known_face_embeddings.append(embedding)
                                known_face_ids.append(face_id)
                                cv2.imwrite(os.path.join(KNOWN_FACES_DIR, f"{face_id}.jpg"), person_crop)
                                next_person_id += 1
                            track_id_to_face_id[track_id] = face_id
                        except: pass
                
                last_pos = track_positions.get(track_id)
                if last_pos is not None and last_pos != current_pos:
                    if current_pos == 1: people_in += 1
                    else: people_out += 1
                track_positions[track_id] = current_pos

                if track_id in track_id_to_face_id:
                    face_id = track_id_to_face_id[track_id]
                    cv2.putText(annotated_frame, face_id, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # --- DISPLAY COUNTERS ON SCREEN ---
    cv2.putText(annotated_frame, f"IN: {people_in}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    cv2.putText(annotated_frame, f"OUT: {people_out}", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
    cv2.putText(annotated_frame, f"ALERTS: {alert_count}", (width - 350, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    cv2.imshow(WINDOW_NAME, annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()