import numpy as np
import cv2

img = cv2.imread('testset/logo.jpg')

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
img = cv2.rectangle(grayscaled, (250, 70), (330, 150), (0,255,0), 2)

cv2.imshow('Draw01', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

