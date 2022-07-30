import cv2
webcam = cv2.VideoCapture(0)
sayac = 1
while sayac<=100:
    kontrol, çerçeve = webcam.read()
    gri = cv2.cvtColor(çerçeve,cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
    cv2.imshow("webcam",gri)
    cv2.imwrite("p"+str(sayac)+".jpg",gri)
    cv2.waitKey(0)
    sayac+=1
