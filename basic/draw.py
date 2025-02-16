import cv2 as cv
import numpy as np

# Criar uma imagem em branco (preta inicialmente)
blank = np.zeros((500, 500, 3), dtype='uint8')

# Desenhar um retângulo corretamente
cv.rectangle(blank, (70, 100), (400, 400), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
#cv.imshow('Circle', blank)

#cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=3)
#cv.imshow('Line', blank)


cv.putText(blank, "Hello, Wolrd", (130,450), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
cv.destroyAllWindows()
