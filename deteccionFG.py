import cv2

cap= cv2.VideoCapture(0)


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
                cv2.putText(frame,'Triangulo',(x,y-5),1,1,(0,0,0),1)
            elif len(approx) == 4:
                aspect_ratio = float(w)/h
                #print("aspect ratio :",aspect_ratio)
                if 0.5 < aspect_ratio <1.5:
                    cv2.putText(frame,"cuadrado",(x,y-5),1,1,(0,0,0),1)
                else:
                    cv2.putText(frame,"rectangulo",(x,y-5),1,1,(0,0,0),1)

            elif len(approx) ==5:
                cv2.putText(frame,"pentagono",(x,y-5),1,1,(0,0,0),1)
            
            elif len(approx) ==6:
                cv2.putText(frame,"hexagono",(x,y-5),1,1,(0,0,0),1)

            elif len(approx) ==3:
                cv2.putText(frame,"triangulo",(x,y-5),1,1,(0,0,0),1)

            elif len(approx)>=10:
                cv2.putText(frame,"circulo",(x,y-5),1,1,(0,0,0),1)
            
            else :
                cv2.putText(frame,"???",(x,y-5),1,1,(0,0,0),1)
                

            #cv2.drawContours(imgContours,[approx],-1,(110,0,255),2) #dibuja los contornos
            cv2.drawContours(frame,[cnt],-1,(110,0,255),2) #dibuja los contornos


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

cv2.destroyAllWindows()

