# 🛡️ Smart Security & Crowd Monitoring System

An intelligent, real-time surveillance system built with **YOLOv8**, **DeepFace**, and **OpenCV**. This project goes beyond simple crowd counting by incorporating face recognition and automated suspicious behavior analysis to create a proactive security solution.

The system detects and tracks individuals, counts entries and exits, identifies known persons, and automatically flags suspicious activities like **sneaking** and **loitering**. When a threat is detected from an unidentified individual, it triggers an audible alert and saves an image for review.

***
***

## 📋 Table of Contents

- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Configuration](#-configuration)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

## ✨ Key Features

- **👥 Real-time Person Tracking & Counting:** Uses YOLOv8 to accurately detect and track multiple people, maintaining a real-time count of individuals entering and exiting the frame.
- **🙂 Face Recognition:** Distinguishes between known and unknown individuals using DeepFace. New, unidentified faces are automatically saved for future recognition.
- **🧐 Suspicious Behavior Detection:**
  - **Sneaking Alert:** Identifies individuals who are crouching (low bounding box aspect ratio) and moving slowly.
  - **Loitering Alert:** Flags individuals who remain stationary in a specific area for an extended period.
- **🚨 Automated Alert System:** Triggers a distinct audio alarm when an **unidentified** person exhibits suspicious behavior, ensuring immediate attention to potential threats.
- **📸 Smart Image Capture:** Automatically saves a snapshot of any unidentified person who triggers an alert to the `alert_captures/` directory for evidence and review.
- **🖥️ Interactive Dashboard:** Provides a full-screen, annotated video feed displaying bounding boxes, person IDs, face IDs, alert statuses, and IN/OUT counters.

---

## ⚙️ How It Works

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

## 📁 Project Structure

Of course\! A well-written README is essential for any great project. Based on the information you provided and the structure of your project, here is a professionally polished and enhanced version of your README file.

You can copy and paste the following content directly into your `README.md` file on GitHub.

-----

```markdown
# 🛡️ Smart Security & Crowd Monitoring System

An intelligent, real-time surveillance system built with **YOLOv8**, **DeepFace**, and **OpenCV**. This project goes beyond simple crowd counting by incorporating face recognition and automated suspicious behavior analysis to create a proactive security solution.

The system detects and tracks individuals, counts entries and exits, identifies known persons, and automatically flags suspicious activities like **sneaking** and **loitering**. When a threat is detected from an unidentified individual, it triggers an audible alert and saves an image for review.

***
***

## 📋 Table of Contents

- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Configuration](#-configuration)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

## ✨ Key Features

- **👥 Real-time Person Tracking & Counting:** Uses YOLOv8 to accurately detect and track multiple people, maintaining a real-time count of individuals entering and exiting the frame.
- **🙂 Face Recognition:** Distinguishes between known and unknown individuals using DeepFace. New, unidentified faces are automatically saved for future recognition.
- **🧐 Suspicious Behavior Detection:**
  - **Sneaking Alert:** Identifies individuals who are crouching (low bounding box aspect ratio) and moving slowly.
  - **Loitering Alert:** Flags individuals who remain stationary in a specific area for an extended period.
- **🚨 Automated Alert System:** Triggers a distinct audio alarm when an **unidentified** person exhibits suspicious behavior, ensuring immediate attention to potential threats.
- **📸 Smart Image Capture:** Automatically saves a snapshot of any unidentified person who triggers an alert to the `alert_captures/` directory for evidence and review.
- **🖥️ Interactive Dashboard:** Provides a full-screen, annotated video feed displaying bounding boxes, person IDs, face IDs, alert statuses, and IN/OUT counters.

---

## ⚙️ How It Works

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

## 📁 Project Structure

```

Smart\_Crowd\_Monitoring\_System/
│
├── known\_faces/            \# Stores face images of known individuals (e.g., 'Umed.jpg').
├── alert\_captures/         \# Automatically saves snapshots of unidentified alert subjects.
├── main.py                 \# The main script to run the application.
├── requirements.txt        \# A list of all necessary Python dependencies.
└── README.md               \# You are here\!

````

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites
- Python 3.8 or higher
- A webcam connected to your system

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/UmedKumar/Smart_Crowd_Monitoring_System.git](https://github.com/UmedKumar/Smart_Crowd_Monitoring_System.git)
    cd Smart_Crowd_Monitoring_System
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: The YOLOv8 model (`yolov8m.pt`) and DeepFace models will be downloaded automatically on the first run.*

### Usage

1.  **Add Known Faces (Optional):**
    - To enable recognition of specific people, add their pictures (e.g., `YourName.jpg`) to the `known_faces/` folder.
    - Ensure the images are clear and show the face prominently. The filename (without extension) will be used as the person's ID.

2.  **Run the application:**
    ```bash
    python main.py
    ```

3.  **Operation:**
    - The system will open a full-screen window from your webcam.
    - Press the **`q`** key at any time to close the application.
    - Any alert-related images will be saved in the `alert_captures/` folder.

---

## 🔧 Configuration

You can fine-tune the detection sensitivity by modifying the constant values at the top of the `main.py` script:

- `SNEAKING_ASPECT_RATIO_THRESHOLD`: Adjusts how "crouched" a person must be to be considered sneaking.
- `SNEAKING_SPEED_THRESHOLD`: Sets the maximum speed for sneaking behavior.
- `LOITERING_CONFIDENCE_FRAMES`: Defines how many consecutive stationary frames trigger a loitering alert.

---

## 🔮 Future Scope

This project has a strong foundation that can be extended with more advanced features:

- [ ] **Multi-Camera Integration:** Support for processing feeds from multiple cameras simultaneously for wider area coverage.
- [ ] **Cloud Integration:** Store alert data (images, timestamps) on a cloud service for persistent storage and remote access.
- [ ] **Web-Based Dashboard:** Develop a web interface using Flask or Django to view the live feed and alerts from any device.
- [ ] **Advanced Action Recognition:** Train a model to detect more complex actions like fighting, falling, or vandalism.

---

## 👨‍💻 Author

**Umed Kumar**

- [GitHub Profile](https://github.com/UmedKumar)
- [LinkedIn Profile](https://www.linkedin.com/in/your-linkedin-profile/) ```
````
