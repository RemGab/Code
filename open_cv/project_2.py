import cv2
from cvzone.HandTrackingModule import HandDetector
import  cvzone
import os

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(cv2.CAP_PROP_BRIGHTNESS,0)

finger_1 = 4
finger_2 = 8

detector = HandDetector(detectionCon=0.8)

class DragImg():
    def __init__(self,path, posOrigin, imgType):
        
        self.posOrigin = posOrigin
        self.imgType = imgType
        self.path = path
        
        if self.imgType == 'png':
            self.img = cv2.imread(self.path,cv2.IMREAD_UNCHANGED)
        else :
            self.img = cv2.imread(self.path)
            
        self.size = self.img.shape[:2]

    def update(self,cursor):
        ox , oy = self.posOrigin
        h , w =self.size
        
        if ox < cursor[0] < ox+w and oy < cursor[1] < oy+h :
            self.posOrigin = cursor[0] - w//2, cursor[1] - h//2

#ox , oy = 500,200

path = r'C:\python\open_cv\images'
myList = os.listdir(path)
#print(myList)

listImg = []
for x,pathImg in enumerate(myList):
    if 'png' in pathImg:
        imgType = 'png'
    else :
        imgType = 'jpg'
        
    listImg.append(DragImg(f'{path}\{pathImg}',[50+x*300,50],imgType))

#print(len(listImg))

while True :
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands,img = detector.findHands(img, flipType=False)
    
    if hands :
        lmList = hands[0]['lmList']
        cursor = lmList[finger_1]
        length, info, img = detector.findDistance(lmList[finger_1],lmList[finger_2],img)
        #print(length)
        if length < 30 :
            cursor = lmList[finger_1]
            for imgObject in listImg:
                imgObject.update(cursor)
                
    try :            
        
        for imgObject in listImg:
            h, w = imgObject.size
            ox, oy = imgObject.posOrigin
            if imgObject.imgType == 'png':
                img = cvzone.overlayPNG(img,imgObject.img,[ox,oy])
            else:
                img[oy:oy + h,ox:ox + w] = imgObject.img 
            
        # Draw for JPG Image
        
        
           
        
        # Draw for PNG Image
        
    except :
        pass
    
    cv2.imshow('Image', img)
    cv2.waitKey(1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows
        break