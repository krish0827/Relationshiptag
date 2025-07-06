 💞 Real-Time Relationship Tag Detector (1–3 Persons)

This is a fun computer vision project that detects 1 to 3 people using a webcam and randomly assigns them a "relationship" tag like **Friend**, **Lover**, **Married**, etc. It visually shuffles tags above their heads for 2 seconds before finalizing the result.

 🎥 Live Demo
> When 1–3 faces appear in the webcam, the system:
- Begins shuffling relationship tags
- After 2 seconds, shows the locked tag above each face
- Press **`R`** to reshuffle the tag anytime

 🧠 Features

✅ Real-time webcam face detection using **Dlib**  
✅ Fun tag shuffling effect for up to 3 people  
✅ Press **Esc** to exit and **R** to reshuffle  
✅ Smooth OpenCV overlay  
✅ Tags: `Friend`, `Lover`, `Married`, `Stranger`, `Soulmate`, `Bestie`

 🔧 Requirements

- Python 3.7+
- OpenCV (`cv2`)
- Dlib (with face detector support)
- Webcam

🔌 Install Dependencies

pip install opencv-python dlib

🚀 How to Run

python relationship_tag_detector.py

⌨️ Controls
R → Reshuffle tag
Esc → Exit program
