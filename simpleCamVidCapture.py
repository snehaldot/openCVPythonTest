import cv2
import numpy as np
# setup video capture
cap = cv2.VideoCapture(0)
frames = []
# get frame, store in array
while True:
    ret,im = cap.read()
    cv2.imshow('video',im)
    frames.append(im)
    if cv2.waitKey(10) == 27:
        break
frames = np.array(frames)

# check the sizes
print im.shape
print frames.shape
