import numpy as np
import cv2
from matplotlib import pyplot as plt

frameWidth = 480
frameHeight = 480

imgL = cv2.imread('C:/Users/PDR/PycharmProjects/OpenCVProject/Resources/Left.jpg',0)
imgR = cv2.imread('C:/Users/PDR/PycharmProjects/OpenCVProject/Resources/Right.png',0)

imgL = cv2.resize(imgL, (frameWidth, frameHeight))
imgR = cv2.resize(imgR, (frameWidth, frameHeight))

#stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
stereo = cv2.StereoBM_create(numDisparities = 32,blockSize = 5)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()