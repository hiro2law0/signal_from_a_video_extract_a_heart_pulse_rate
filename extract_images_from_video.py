import cv2
import os

# Open the video file
cap = cv2.VideoCapture("output2.mp4")

# Get the video frames per second (fps) and frame size
fps = cap.get(cv2.CAP_PROP_FPS)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Calculate the number of frames in the first 30 seconds of the video
total_frames = int(fps * 30)

# Create a directory to store the extracted frames
os.makedirs("frames", exist_ok=True)

# Loop over the first 30 seconds of the video
for i in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break

    # Save the frame as an image
    filename = f"frames/frame_{i:05d}.jpg"
    cv2.imwrite(filename, frame)

# Release the video capture object
cap.release()
