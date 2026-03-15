import cv2 as cv

while True:
    img_input = input("Input your image directory below")
    median = cv.medianBlur(img_input)
    cv.imshow('Median Blur', median)
    print("Viola! Press 0 to exit program.")
    

cv.waitKey(0)
#aaaaaaaaaabububiubhdi ijdoijasoidjidjio jdoijddddddd