import cv2
import numpy as np

img=cv2.imread('src/figGeometricas.png')
imgContours=img.copy()
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

cv2.imshow("figuras",img)
cv2.imshow("figuras gris",imgGray)
cv2.imshow("figuras en blur",imgBlur)
cv2.imshow("figuras en Cnny",imgCanny)
cv2.imshow("fig contornos",imgContours)


cv2.waitKey(0)
cv2.destroyAllWindows()



