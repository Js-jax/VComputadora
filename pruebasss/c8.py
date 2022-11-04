import cv2
import numpy as np 
 
kernel = np.ones((5,5), np.uint8) 

capture = cv2.VideoCapture(0);

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        #Escala de grises
        frame = cv2.flip(frame,1)
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Suavizado Gausiano
        gauss = cv2.GaussianBlur(gris, (5,5), 0)
        
        
        #Erosion a Gausiano
        img_erosion = cv2.erode(gauss, kernel, iterations=1) 
        img_dilation = cv2.dilate(gauss, kernel, iterations=1)
     
        #Dteccion de bordes Canny
        canny = cv2.Canny(img_erosion, 80, 180)

        #Contornos
        (contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        
        #Mostrar Ventanas
        cv2.imshow("Ventana", frame)
        cv2.imshow("gris", gris)
        cv2.imshow("suavizado", gauss)
        cv2.imshow('Erosion', img_erosion) 
        cv2.imshow("canny", canny)
        cv2.drawContours(frame,contornos,-1,(0,0,255), 2)
        cv2.imshow("Contornos", frame)
 
        
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()