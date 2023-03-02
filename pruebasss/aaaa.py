import cv2
import numpy as np
kernel = np.ones((5,5), np.uint8) 
 
# Cargamos la imagen
original = cv2.imread("ej11.jpeg")
cv2.imshow("original", original)


 
# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

cv2.imshow("gris", gris)
 
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (5,5), 0)
 
cv2.imshow("suavizado", gauss)

  
img_erosion = cv2.erode(gauss, kernel, iterations=1) 
img_dilation = cv2.dilate(gauss, kernel, iterations=1)

cv2.imshow('Erosion', img_erosion) 
#cv2.imshow('Dilation', img_dilation)

 
# Detectamos los bordes con Canny
canny = cv2.Canny(img_erosion, 80, 180)
 
cv2.imshow("canny", canny)
 
# Buscamos los contornos
(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
# Mostramos el número de monedas por consola
print("Piedras {} ".format(len(contornos)))
 
cv2.drawContours(original,contornos,-1,(0,0,255), 2)
cv2.imshow("Piedras", original)
 
cv2.waitKey(0)
