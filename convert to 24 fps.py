import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture("video_signal.mp4")

# Get the video frames per second (fps) and frame size
fps = cap.get(cv2.CAP_PROP_FPS)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Define the desired output frame rate and the codec
output_fps = 24.0
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Create a video writer object
out = cv2.VideoWriter("output.mp4", fourcc, output_fps, frame_size)

# Create a buffer to store the previous frame
previous_frame = None

# Loop over the frames of the input video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Skip every (fps / output_fps) - 1 frame
    if previous_frame is not None and (fps / output_fps) > 1.5:
        skip_frame = int(fps / output_fps) - 1
        for i in range(skip_frame):
            cap.grab()
    else:
        # Interpolate the frame to match the desired output frame rate
        if previous_frame is not None:
            frame = (previous_frame + frame) / 2.0
        previous_frame = frame

    # Write the frame to the output video
    out.write(np.uint8(frame))

# Release the video capture and writer objects
cap.release()
out.release()
