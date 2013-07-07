import cv2.cv
from cv2 import *
cv.NamedWindow("camera", 1)

capture = cv.CaptureFromCAM(-1)

while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    if cv.WaitKey(10) == 27:
        break
