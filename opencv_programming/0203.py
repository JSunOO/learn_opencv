# 0203.py
import cv2
from matplotlib import pyplot as plt

imgFile = './data/lena.jpg'
imgBGR = cv2.imread(imgFile)
plt.axis('off')

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)

plt.show()