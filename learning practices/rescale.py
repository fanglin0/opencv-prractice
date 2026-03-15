import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('cat', img)

#image, videos, live video
def rescaleFrame(frame, scale =0.75): #deafult is 0.75
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

#live video only (external cam/webcam. doesnt work on existing vuideo)
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height) #set this to 10 to change brightness




resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

#reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale = 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)