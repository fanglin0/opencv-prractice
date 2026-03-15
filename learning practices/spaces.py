import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR TO RBG
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV TO BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR', lab_bgr)

plt.imshow(rgb)
plt.show()

#use LAB and contorus to find seasonal color


cv.waitKey(0)