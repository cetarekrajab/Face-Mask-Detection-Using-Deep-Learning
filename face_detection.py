import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load Mask Detection Model
model = load_model("mask_detection_model_v2.keras")

# Load Built-in Face Detector (NO FILE ERROR)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml'
)

# Start Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

print("Press 'q' to quit")

# Real-Time Detection Loop
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Improved detection settings
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        # Add margin (important for mask area)
        margin = 20
        x1 = max(0, x - margin)
        y1 = max(0, y - margin)
        x2 = x + w + margin
        y2 = y + h + margin

        face = frame[y1:y2, x1:x2]

        if face.size == 0:
            continue

        # Preprocess for model
   
        face = cv2.resize(face, (224, 224))
        face = face / 255.0
        face = np.reshape(face, (1, 224, 224, 3))

   
        # Prediction
        prediction = model.predict(face, verbose=0)
        label = np.argmax(prediction)

        if label == 0:
            text = "Mask On"
            color = (0, 255, 0)
        else:
            text = "No Mask"
            color = (0, 0, 255)

        # Draw results
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Mask Detection Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()