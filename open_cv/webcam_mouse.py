import cv2
import numpy as np
import time
import autopy
from cvzone.HandTrackingModule import HandDetector


#####################################################
wCam, hCam = 1280,800 
frameR = 300 #Frame Reduction
smoothening = 5
#####################################################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
pLocX, pLocY = 0,0.
cLocX, cLocY = 0,0
detector = HandDetector(detectionCon =0.5,maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr,hScr)





while True : 
    # 1 Trouver la structure de la main
    success, img = cap.read()
    hands, img = detector.findHands(img)
    # 2 Avoir le bout de l'index et du doigt middle
    try : 
        if hands :
            hand1=hands[0]
            lmList1 = hand1['lmList']
            bbox1 = hand1['bbox'] 
            x1, y1 = lmList1[8]
            x2, y2 = lmList1[12]
            finger1 = lmList1[8]
            finger2 = lmList1[12]
        # 3 Check si doigt debout
            fingers = detector.fingersUp(hand1)
            cv2.rectangle(img,(frameR, frameR),(wCam-frameR, hCam-frameR),(255,0,255))
            # print(fingers)
            
            # 4 Juste un doigt : moving mode
            if fingers[1]==1 and fingers[2] == 0:
                # 5 Convertir coordonnées
                x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
                y3 = np.interp(y1,(frameR,hCam-frameR),(0,hScr))
                cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
                # 6 Smoothen values
                cLocX = pLocX +(x3-pLocX)/smoothening
                cLocY = pLocY +(y3-pLocY)/smoothening
                
                # 7 Move mouse
                autopy.mouse.move(wScr-cLocX,cLocY)
                
                pLocX,pLocY = cLocX, cLocY
        # 8 Detecter si les deux doigts sont debouts
            if fingers[1]==1 and fingers[0] == 1:
                    
                autopy.mouse.click()
                time.sleep(0.3)
            
            if fingers[0:5] == [1,1,0,0,1] :
                break
             
        # 9 Trouver distance entre les deux doigts
        # 10 Click mouse if distance short
        # 11 Frame rate
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    except:
        pass
    # 12 Afficher
    cv2.imshow('Image',img)

    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cv2.destroyAllWindows()