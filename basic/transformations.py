import cv2 as cv
import numpy as np


img = cv.imread(r'C:\Users\Karllos\Desktop\OpenCV\recursos\photos\cat.jpg')
cv.imshow('Image', img)
#funcao que desloca a imagem nos eixos x y
def translate (img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100,100)
cv.imshow('Translated', translated)


#rotation 
def rotate(img, angle, rotPoint=None):
    (heigth, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, heigth//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, heigth)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

#inverte a imagem
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

#corte
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)