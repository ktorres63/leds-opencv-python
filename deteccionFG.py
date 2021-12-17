from contextlib import nullcontext
import cv2
import serial
import time
import numpy as np

cap= cv2.VideoCapture(2) #probar nums 

#coneccion arduino
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)

time.sleep(2)



def getContours(img):
    contours, hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:

            epsilon=0.01*cv2.arcLength(cnt,True) 
            approx= cv2.approxPolyDP(cnt,epsilon,True)
            x,y,w,h = cv2.boundingRect(approx)

            if len(approx)==3:
                cv2.putText(frame,'Triangulo',(x,y-5),1,1,(0,0,0),1)
                ser.write(b't')

            elif len(approx) == 4:
                aspect_ratio = float(w)/h
                #print("aspect ratio :",aspect_ratio)
                if 0.5 < aspect_ratio <1.5:
                    cv2.putText(frame,"Cuadrado",(x,y-5),1,1,(0,0,0),1)
                    ser.write(b'c')

                else:
                    cv2.putText(frame,"Rectangulo",(x,y-5),1,1,(0,0,0),1)
                    ser.write(b'r')
                    
            elif len(approx) ==5:
                cv2.putText(frame,"Pentagono",(x,y-5),1,1,(0,0,0),1)
                ser.write(b'p')
                
            elif len(approx) ==6:
                cv2.putText(frame,"Hexagono",(x,y-5),1,1,(0,0,0),1)
                ser.write(b'x')
                
            elif len(approx)>=10:
                cv2.putText(frame,"Circulo",(x,y-5),1,1,(0,0,0),1)
                ser.write(b'i')
               
            else :
                cv2.putText(frame,"???",(x,y-5),1,1,(0,0,0),1)
                ser.write(b'?')
                
            cv2.drawContours(frame,[approx],-1,(110,0,255),2) #dibuja los contornos

        

while True:
    ret,frame = cap.read()
    if ret == False: break
    frame = cv2.flip(frame,1)

    imgGray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    imgBlur= cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    imgCanny = cv2.dilate(imgCanny,None,iterations=1)
    imgCanny= cv2.erode(imgCanny,None,iterations=1)
    

    getContours(imgCanny)


    cv2.imshow("fig contornos",frame)

    if cv2.waitKey(1)==27: #con esc
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
