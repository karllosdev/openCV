import cv2 as cv

img = cv.imread(r"C:\Users\Karllos\Desktop\OpenCV\recursos\photos\cat.jpg")
cv.imshow('Cat', img) #exibe a imagem

def rescaleFrame(frame, scale=0.75): #recebe uma imagem
    #.shape é uma tupla que possui [(ALTURA, LARGURA, COR)]
    width = int(frame.shape[1]* scale) #frame.shape[1] indica largura
    height = int(frame.shape[0]* scale) #frame.shape[0] indica altura

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #INTER_AREA EVITA A PERCA DE RESOLUCAO


resized_image = rescaleFrame(img)

cv.imshow('Image', resized_image)

cv.waitKey(0)