import cv2 as cv
import numpy as np
img = cv.imread("Resources/Photos/park.jpg")
cv.imshow('Park', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
#-x --> left
#-y --> up
#x --> right
#y --> down

translated= translate(img,-100,-100)
cv.imshow('Translated', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,-45)
#pos degree is counter-clockwise, neg is clockwise
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow("Rotated rotated", rotated_rotated)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#flipping
#1 is horizontal, 0 vertical, -1 both
flip = cv.flip(img, -1)
cv.imshow("Flip", flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)
cv.waitKey(0)

