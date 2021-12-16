import cv2
import numpy as np


def getContours(img):
    contours, hierarchy=cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area > 500:
            #perimetro=cv2.arcLength(cnt,True) 
            epsilon=0.01*cv2.arcLength(cnt,True) 
            approx= cv2.approxPolyDP(cnt,epsilon,True)
            #print(epsilon)
            #print(len(approx))
            
            x,y,w,h = cv2.boundingRect(approx)
            
            if len(approx)==3:
                cv2.putText(imgContours,'Triangulo',(x,y-5),1,1,(0,255,0),1)
            elif len(approx) == 4:
                aspect_ratio = float(w)/h
                #print("aspect ratio :",aspect_ratio)
                if 0.5 < aspect_ratio <1.5:
                    cv2.putText(imgContours,"cuadrado",(x,y-5),1,1,(0,255,0),1)
                else:
                    cv2.putText(imgContours,"rectangulo",(x,y-5),1,1,(0,255,0),1)

            elif len(approx) ==5:
                cv2.putText(imgContours,"pentagono",(x,y-5),1,1,(0,255,0),1)
            
            elif len(approx) ==6:
                cv2.putText(imgContours,"hexagono",(x,y-5),1,1,(0,255,0),1)

            elif len(approx) ==3:
                cv2.putText(imgContours,"triangulo",(x,y-5),1,1,(0,255,0),1)

            elif len(approx)>=10:
                cv2.putText(imgContours,"circulo",(x,y-5),1,1,(0,255,0),1)
            
            else :
                cv2.putText(imgContours,"???",(x,y-5),1,1,(0,255,0),1)
                

            cv2.drawContours(imgContours,[approx],-1,(110,0,255),2) #dibuja los contornos



img=cv2.imread('src/figGeometricas.png')
imgContours=img.copy()
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgCanny = cv2.dilate(imgCanny,None,iterations=1)
imgCanny= cv2.erode(imgCanny,None,iterations=1)

getContours(imgCanny)

#cv2.imshow("figuras",img)
#cv2.imshow("figuras gris",imgGray)
#cv2.imshow("figuras en blur",imgBlur)
#cv2.imshow("figuras en Cnny",imgCanny)
cv2.imshow("fig contornos",imgContours)

cv2.waitKey(0)
cv2.destroyAllWindows()

