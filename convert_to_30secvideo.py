import cv2

# Open the video file
cap = cv2.VideoCapture("output.mp4")

# Get the video frames per second (fps) and frame size
fps = cap.get(cv2.CAP_PROP_FPS)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Calculate the number of frames in the first 30 seconds of the video
total_frames = int(fps * 30)

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output2.mp4", fourcc, fps, frame_size)

# Loop over the first 30 seconds of the video
for i in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break

    # Write the frame to the output video
    out.write(frame)

# Release the video capture and writer objects
cap.release()
out.release()
