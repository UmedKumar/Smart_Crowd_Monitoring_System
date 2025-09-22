# Smart Crowd Monitoring System

This project implements a real-time **crowd monitoring and security system** using **YOLOv8, DeepFace, and OpenCV**. It detects and tracks individuals, recognizes faces, identifies suspicious behaviors such as sneaking and loitering, and triggers automated alerts with image captures for unidentified persons.  

The system is designed for surveillance applications where real-time crowd analysis and proactive threat detection are essential.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Methodology](#methodology)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Project Overview
Crowd safety and security are critical in public spaces, events, and restricted areas. Traditional surveillance systems often lack real-time intelligence and automated response mechanisms.  

This project integrates **object detection, face recognition, and behavior analysis** to provide a smart solution for monitoring crowds. By detecting suspicious activity (sneaking or loitering) and raising real-time alerts, it enhances situational awareness and reduces response time during security incidents.

---

## Features
- **Real-time Detection & Tracking:** Detects and tracks people using YOLOv8 with entry/exit counting.  
- **Face Recognition:** Identifies known vs. unknown individuals using DeepFace embeddings.  
- **Suspicious Behavior Detection:** Detects sneaking (unusual movement posture) and loitering (extended stationary presence).  
- **Automated Alerts:** Triggers audio alarms and saves snapshots of unidentified persons during alerts.  
- **Security Dashboard:** Annotated video feed with counters (IN, OUT) and alerts for monitoring.  

---

## Methodology

1. **Person Detection and Tracking:**  
   - YOLOv8 is used to detect people in video frames.  
   - Tracking ensures continuity of individuals across frames with unique IDs.  

2. **Face Recognition:**  
   - DeepFace generates embeddings for detected faces.  
   - Faces are matched against a database of known individuals.  
   - Unknown faces are stored automatically for future reference.  

3. **Behavior Analysis:**  
   - **Sneaking Detection:** Based on aspect ratio and low movement speed.  
   - **Loitering Detection:** Based on low speed maintained over extended frames.  

4. **Alerts and Logging:**  
   - Automated beeps for critical alerts (unrecognized sneaking).  
   - Snapshots of unidentified individuals saved in an alert directory.  
   - Real-time overlay showing identity, alerts, and counters.  

---

## Project Structure

Smart_Crowd_Monitoring_System/
│── known_faces/ # Stores known individuals’ face images
│── alert_captures/ # Stores snapshots of unidentified individuals during alerts
│── main.py # Main script for running the system
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/UmedKumar/Smart_Crowd_Monitoring_System.git
   cd Smart_Crowd_Monitoring_System
pip install -r requirements.txt
Install dependencies:
pip install -r requirements.txt
Download YOLOv8 model (if not already present):
yolo download yolov8m.pt

## Usage

*Run the system:

*python main.py

- Press q to exit the application.
- Place known faces in the known_faces/ directory for identification.
- Snapshots of unidentified persons will be saved in alert_captures/.

## Future Improvements

- Multi-camera integration for large-scale monitoring.
- Cloud storage for alerts and captured data.
- Web-based dashboard for remote access and control.
- Improved accuracy with advanced embedding models.


## Author

Umed Kumar – [GitHub Profile](https://github.com/UmedKumar)


--- 
