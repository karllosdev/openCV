import cv2 as cv

img = cv.imread(r"C:\Users\Karllos\Desktop\OpenCV\recursos\photos\cat_large.jpg")
cv.imshow('Cat', img)

cv.waitKey(0)

