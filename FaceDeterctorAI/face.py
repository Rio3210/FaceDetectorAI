import cv2 
detect=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
webcam=cv2.VideoCapture(0)
while True:
    successful,frame=webcam.read()
    grasc_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facord=detect.detectMultiScale(grasc_img)

    for (x,y,w,h) in facord:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("My frontal face detector",frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break
webcam.release()
