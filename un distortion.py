import numpy as np
import cv2 as cv
import glob
for image in glob.glob('D:/21R435/resources/Calib/CaliResult*.png'):

    img = cv.imread(image)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #ret, corners = cv.findChessboardCorners(gray, (24,17),None)
    ret, corners = cv.findChessboardCorners(gray, (9,6), None)

    if ret == True:
        print('Pose Estimation Started')
        corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1), criteria)
        #print(corners2)

        # Find the rotation and translation vectors.
        ret, rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)

        # Project 3D points to image plane
        imgpts, jac = cv.projectPoints(axisBoxes, rvecs, tvecs, mtx, dist)

        img = drawBoxes(img,corners2,imgpts)
        cv.imshow('img',img)

       # k = cv.waitKey(0)
       # if k == ord('s'):
    cv.imwrite('pose.png', img)
cv.waitKey(0)


#cv.destroyAllWindows()