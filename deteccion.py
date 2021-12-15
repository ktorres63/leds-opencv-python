import cv2
import serial
import time 

# carga la cascada
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# capturamos el video
cap = cv2.VideoCapture(0)

#conecta arduino y python
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)

time.sleep(2)


while True:
     _,img = cap.read()         #usamos _ para ignorar el primer valor
     
     #convertimos a escala de grises
     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray,1.1,4) # detecta rostros
     
     #cv2.putText(img,'hola',(0,255),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
     
     texto = "Hola"
     ubicacion = (0,225)
     font = cv2.FONT_HERSHEY_TRIPLEX
     tamañoLetra = 1
     colorLetra = (221,82,196)
     grosorLetra = 2

     #Escribir texto
     cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
     #cv2.imshow('text',img)

     print(faces)
     if type(faces)==tuple:
          ser.write(b'P')
     else:
          ser.write(b'N')


     for (x,y,w,h) in faces:
          cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

     
     cv2.imshow('img',img)
     #print(type(faces))

     k = cv2.waitKey(30) # si apretas esc se cierra
     if k == 27:
          ser.write(b'X')
          break

cap.release()
cv2.destroyAllWindows()
ser.close()