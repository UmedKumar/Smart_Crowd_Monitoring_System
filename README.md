# 🛡️ Smart Security & Crowd Monitoring System

An intelligent, real-time surveillance system built with **YOLOv8**, **DeepFace**, and **OpenCV**. This project goes beyond simple crowd counting by incorporating face recognition and automated suspicious behavior analysis to create a proactive security solution.

The system detects and tracks individuals, counts entries and exits, identifies known persons, and automatically flags suspicious activities like **sneaking** and **loitering**. When a threat is detected from an unidentified individual, it triggers an audible alert and saves an image for review.

***
***

## Table of Contents

- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

## Key Features

- **Real-time Person Tracking & Counting:** Uses YOLOv8 to accurately detect and track multiple people, maintaining a real-time count of individuals entering and exiting the frame.
- **Face Recognition:** Distinguishes between known and unknown individuals using DeepFace. New, unidentified faces are automatically saved for future recognition.
- **Suspicious Behavior Detection:**
  - **Sneaking Alert:** Identifies individuals who are crouching (low bounding box aspect ratio) and moving slowly.
  - **Loitering Alert:** Flags individuals who remain stationary in a specific area for an extended period.
- **Automated Alert System:** Triggers a distinct audio alarm when an **unidentified** person exhibits suspicious behavior, ensuring immediate attention to potential threats.
- **Smart Image Capture:** Automatically saves a snapshot of any unidentified person who triggers an alert to the `alert_captures/` directory for evidence and review.
- **Interactive Dashboard:** Provides a full-screen, annotated video feed displaying bounding boxes, person IDs, face IDs, alert statuses, and IN/OUT counters.

---

## How It Works

The system operates through a sequential pipeline for each frame of the video feed:

1.  **Person Detection:** The YOLOv8 model processes the video frame to detect all persons present.
2.  **Tracking:** Each detected person is assigned a unique tracking ID that persists across frames.
3.  **Behavior Analysis:** For each tracked person, the system calculates:
    - **Speed:** By tracking the center point of the bounding box between frames.
    - **Aspect Ratio:** The height-to-width ratio of the bounding box is used to infer posture (e.g., crouching vs. standing).
4.  **Face Recognition:**
    - If a person is newly tracked, their face is cropped from the frame.
    - **DeepFace** generates a facial embedding (a vector representation of the face).
    - This embedding is compared against a database of pre-saved embeddings in the `known_faces/` directory.
    - If no match is found, the person is labeled as a new "Person" and their face is saved to the database.
5.  **Alert Trigger:** An alert is triggered if a person's movement and posture match the predefined thresholds for "sneaking" or "loitering." The system then checks if the person is unidentified.
6.  **Visualization & Action:** The final frame is annotated with all the collected information (boxes, IDs, counters, alert text) and displayed. If an alert condition is met, an audio beep is played and an image is saved.

---

## Project Structure

```

Smart\_Crowd\_Monitoring\_System/
├── known\_faces/           \ Stores face images of known individuals (e.g., 'sample.jpg').
├── alert\_captures/        \ Automatically saves snapshots of unidentified alert subjects.
├── main.py                 \ The main script to run the application.
├── requirements.txt        \ A list of all necessary Python dependencies.
└── README.md               \ You are here\!

```

---

## 🔮 Future Scope

This project has a strong foundation that can be extended with more advanced features:

- [ ] **Multi-Camera Integration:** Support for processing feeds from multiple cameras simultaneously for wider area coverage.
- [ ] **Cloud Integration:** Store alert data (images, timestamps) on a cloud service for persistent storage and remote access.
- [ ] **Web-Based Dashboard:** Develop a web interface using Flask or Django to view the live feed and alerts from any device.
- [ ] **Advanced Action Recognition:** Train a model to detect more complex actions like fighting, falling, or vandalism.

---

## Author

**Umed Kumar**

- [GitHub Profile](https://github.com/UmedKumar)

```
