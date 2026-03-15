import cv2 as cv

img = cv.imread('Resources/Photos/cat_large2.jpg')
cv.imshow('cat', img) #displays image in new window
cv.waitKey(0)

# reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()


# 215 error is path error


