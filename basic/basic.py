import cv2 as cv

img  = cv.imread(r"C:\Users\Karllos\Desktop\OpenCV\recursos\photos\cat.jpg")
cv.imshow('Image', img)

#convertendo em tons de cinza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('GRAY', gray)

#desfoque gaussiano
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#cascatas (bordas)
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)

#eDilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

#eroding 
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resize', resized)

#Corte
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)