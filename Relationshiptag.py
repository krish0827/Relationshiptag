#more tham one face with shuffle

import cv2
import dlib
import random
import time

# Initialize Dlib face detector
detector = dlib.get_frontal_face_detector()

# Tags
TAGS = ['Friend', 'Lover', 'Married', 'Stranger', 'Soulmate', 'Bestie']
current_tag = ""
finalized = False
shuffle_start_time = None
shuffle_duration = 2  # seconds

# Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    face_count = len(faces)

    # --- Main Logic: 1 to 3 faces ---
    if 1 <= face_count <= 3:
        if not finalized:
            if shuffle_start_time is None:
                shuffle_start_time = time.time()

            elapsed = time.time() - shuffle_start_time
            if elapsed < shuffle_duration:
                current_tag = random.choice(TAGS)
            else:
                random.shuffle(TAGS)
                current_tag = TAGS[0]
                finalized = True

        # Draw on each face
        for face in faces:
            x, y, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, current_tag, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    else:
        # More than 3 faces or 0 — ignore
        current_tag = ""
        finalized = False
        shuffle_start_time = None
        cv2.putText(frame, "Waiting for faces...", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Show window
    cv2.imshow("Relationship Tag", frame)

    # Controls
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        break
    elif key == ord('r'):
        finalized = False
        shuffle_start_time = None
        current_tag = ""

cap.release()
cv2.destroyAllWindows()
