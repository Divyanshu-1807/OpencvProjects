import cv2
import autopy
import numpy as np
from cvzone.HandTrackingModule import HandDetector

frame=100
plocx,plocy=0,0
clox,clocy=0,0
smoothing=25
wscr,hscr=autopy.screen.size()
wcam=640
hcam=480
cap=cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
detector=HandDetector(maxHands=1)

while True:
    success,img=cap.read()
    lmlist,bbox=detector.findHands(img)
    for list in lmlist:
        llist=list.get("lmList")
        x1=llist[8][0]
        y1=llist[8][1]

        x2=np.interp(x1,(frame,wcam-frame),(0,wscr+25))
        y2=np.interp(y1,(frame,hcam-frame),(0,hscr+25  ))

        clocx=plocx+(x2-plocx)/smoothing
        clocy=plocy+(y2-plocy)/smoothing

        fingers=detector.fingersUp(lmlist[0])
        if fingers[1]==1:
            autopy.mouse.move(wscr-clocx,clocy)
            cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)    
            plocx,plocy=clocx,clocy

        if fingers[1]==1 and fingers[2]==1:
            #len,img,lineinfo=detector.findDistance(8,12,img)
            len=llist[8][0]-llist[12][0]
            if len<30:
                autopy.mouse.click()

    cv2.imshow("VIRTUAL MOUSE",img)
    if cv2.waitKey(1)==ord('q'):
        break