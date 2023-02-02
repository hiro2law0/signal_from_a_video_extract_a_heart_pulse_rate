import cv2
import numpy as np

# Load the Haar cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Loop through the set of images
for i in range(1, 1801):
    # Load the image
    img = cv2.imread(f"frame_{i:05d}.jpg")

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image using the Haar cascade classifier
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save the result
    cv2.imwrite(f"facesframe_{i:05d}.jpg", img)
