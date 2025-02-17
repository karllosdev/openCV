import cv2 as cv
img = cv.imread(r"C:\Users\Karllos\Desktop\OpenCV\recursos\photos\park.jpg")
cv.imshow('cats', img)

average = cv.blur(img,(7,7))
cv.imshow('Avarage', average)

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('GaussianBlur', gauss)

median = cv.medianBlur(img, 7)
cv.imshow('medianBlur', median)

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral) 

cv.waitKey(0)