import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

#adaptive thresholding ddddddddddddddddddddddddddddddddddddddddddddddd
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 5)
cv.imshow('Adaptive Thresholded', adaptive_thresh)

cv.waitKey(0)