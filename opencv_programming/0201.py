#0201.py
import cv2
import numpy as np

imageFile = './data/lena.png'
img = cv2.imread(imageFile)
img2 = cv2.imread(imageFile, 0)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey()
cv2.destroyAllWindows()