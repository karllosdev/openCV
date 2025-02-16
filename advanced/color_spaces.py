import cv2 as cv
import matplotlib.pyplot as plt

img =  cv.imread(r"C:\Users\Karllos\Desktop\OpenCV\recursos\photos\cat.jpg")
cv.imshow('Image', img)

plt.imshow(img)
plt.show()

gray = cv. cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)


cv.waitKey(0)