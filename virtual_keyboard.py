import time
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,480)
detector=HandDetector(detectionCon=0.8)

def keyboard(x,y,txt):
      cvzone.cornerRect(img,(x,y,70,70),20,rt=0)
      cv2.rectangle(img,(x,y),(x+70,y+70),(255,0,0),cv2.FILLED)
      if(txt=="BCK"):
            cv2.putText(img,txt,(x+5,y+45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
      else:
            cv2.putText(img,txt,(x+25,y+45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

button0=[(80,120,"1"),(160,120,"2"),(240,120,"3"),(320,120,"4"),(400,120,"5"),(480,120,"6"),(560,120,"7"),(640,120,"8"),(720,120,"9"),(800,120,"0")]
button1=[(100,200,"Q"),(180,200,"W"),(260,200,"E"),(340,200,"R"),(420,200,"T"),(500,200,"Y"),(580,200,"U"),(660,200,"I"),(740,200,"O"),(820,200,"P")]
button2=[(120,280,"A"),(200,280,"S"),(280,280,"D"),(360,280,"F"),(440,280,"G"),(520,280,"H"),(600,280,"J"),(680,280,"K"),(760,280,"L"),(840,280,"_")]
button3=[(140,360,"Z"),(220,360,"X"),(300,360,"C"),(380,360,"V"),(460,360,"B"),(540,360,"N"),(620,360,"M"),(700,360,","),(780,360,"."),(860,360,"BCK")]
buttons=[button0,button1,button2,button3]

def number(): 
      for x,y,z in button0:
            keyboard(x+50,y,z)

def front():
      for x,y,z in button1:
            keyboard(x+50,y,z)

def middle():
     for x,y,z in button2:
            keyboard(x+50,y,z)

def last():
     for x,y,z in button3:
            keyboard(x+50,y,z)

text=" "
pre=""
while(True):
      success,img=cap.read()
      lmlist,bbox=detector.findHands(img)      
      #detector.findPosition(img)
      #if 100<llist[1][8]<160 and 200<llist[8][1]<260:
      #     cv2.rectangle(img,(100,200),(160,260),(0,255,0),cv2.FILLED)
      #    cv2.putText(img,"Q",(120,240),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)      
      number()
      front()
      middle()
      last()
      for list in lmlist:
            llist=list.get("lmList")
            #print(llist[8][0])
            for button in buttons:
                  for x,y,z in button: 
                        if(x<llist[8][0]<x+70 and y<llist[8][1]<y+70):
                              cv2.rectangle(img,(x+50-7,y-7),(x+50+70+7,y+70+7),(0,255,0),cv2.FILLED)
                              if(z=="BCK"):
                                    cv2.putText(img,z,(x+50+5,y+45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                              else:   
                                    cv2.putText(img,z,(x+50+25,y+45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                              l=llist[8][0]-llist[12][0]
                              if(l<50):
                                    cv2.rectangle(img,(x+50-7,y-7),(x+50+70+7,y+70+7),(255,0,225),cv2.FILLED)
                                    if(z=="BCK"):
                                          cv2.putText(img,z,(x+50+5,y+45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                    else: 
                                          cv2.putText(img,z,(x+50+25,y+45),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                                    if(z=="_"):
                                          text+=" "
                                    elif(z=="BCK"):
                                          text=text[:len(text)-1]
                                    else:
                                          text+=z
                                          pre=z 
                                    time.sleep(0.5)
                              #print(l)
      cv2.rectangle(img,(150,500),(1000,600),(255,0,0),cv2.FILLED)
      cv2.putText(img,text,(150,570),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
      cv2.imshow("VR KEYBOARD",img)
      if cv2.waitKey(1)==ord('q'):
            break
      