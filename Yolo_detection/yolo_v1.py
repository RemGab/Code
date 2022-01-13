from ast import While
from sre_constants import SUCCESS
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow('image',img)
    cv2.waitKey(1)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
