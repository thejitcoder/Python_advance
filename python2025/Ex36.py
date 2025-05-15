import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Get the default video frame width and height
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
# 'XVID' is a popular codec; you can also try 'MJPG' or 'MP4V'
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('D:/output.avi', fourcc, 20.0, (frame_width, frame_height), isColor=False)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Write the frame to the output file
    out.write(gray)

    # Display the grayscale video
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

# Release everything when done
cap.release()
out.release()
cv.destroyAllWindows()