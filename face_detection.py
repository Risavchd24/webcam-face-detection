import cv2
import time
import os
casc = 'front_face_cascade1.xml'
facecasc = cv2.CascadeClassifier(casc)
vid = cv2.VideoCapture(0)
while True :
    ret,frame = vid.read()
    faces = facecasc.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
         )
    
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
    frame = cv2.flip(frame,1)
    cv2.imshow("FACE DETECTED",frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    
vid.release()
cv2.destroyAllWindows()
