# Real-Time-Face-Detection
📌 Overview
This project demonstrates a real-time face and facial feature detection system using Python and OpenCV’s Haar Cascade Classifiers.
It detects a face, eyes, nose, and mouth from a live webcam stream and highlights them with bounding boxes and labels.

The code is designed for clarity, reusability, and extendability, making it a good base for experimenting with more advanced computer vision tasks.

🚀 Features
Real-time video stream processing

Face detection using Haar cascades

Eye, nose, and mouth detection within the detected face region

Modular and reusable helper functions for boundary drawing and detection

Easily extendable for other Haar cascades or custom-trained models

📂 Project Structure
pgsql
Copy
Edit
.
├── haarcascade_frontalface_default.xml
├── haarcascade_eye.xml
├── Nariz.xml
├── Mouth.xml
├── face_detection.py
└── README.md
face_detection.py — Main Python script to run the detection pipeline.

*.xml — Haar cascade XML files for face, eyes, nose, and mouth detection.

🧰 Requirements
Python 3.x

OpenCV (cv2)

Install dependencies:

bash
Copy
Edit
pip install opencv-python
⚙️ How It Works
Initialize Classifiers:
Pre-trained Haar cascades are loaded for detecting the face, eyes, nose, and mouth.

Capture Video:
The script uses your default webcam (VideoCapture(0)).

Process Each Frame:

Convert the frame to grayscale (Haar cascades perform better on grayscale images).

Detect the face region.

If a face is found, detect eyes, nose, and mouth within that region.

Draw rectangles and label each detected feature.

Display Output:
The annotated video feed is shown in real-time.
Press q to exit gracefully.

📝 Usage
Make sure all the required XML files are in the same directory as the script.

Run:

bash
Copy
Edit
python face_detection.py
A window will open showing your webcam feed with detected face and features highlighted.

Press q to quit.

⚠️ Notes
Haar cascades are fast but may produce false positives; for more robust performance, consider switching to DNNs or HOG-based detectors.

Make sure your XML files are valid and in the correct path.

Detection accuracy heavily depends on lighting and webcam quality.

✅ Best Practices Applied
Modular Functions: draw_boundary() and detect() keep the code organized and maintainable.

Comments and Docstrings: Each method has clear explanations.

Color Coding: Each feature has a unique color for easy visualization.

Graceful Exit: Resources are released properly after execution.

📚 Next Steps
If you wish to take this further:

Use DNN-based detectors like OpenCV’s DNN module or Mediapipe.

Integrate face recognition or emotion detection.

Add snapshot saving or video recording capabilities.

✨ Author
Developed and maintained by Suman Dumre.

📜 License
This project is released under the MIT License — feel free to use and modify it as you wish.
