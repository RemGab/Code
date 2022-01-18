from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time
import autopy

width, heigth = autopy.screen.size()
width, heigth = int(width), int(heigth)

mon = {'top': 0, 'left':0, 'width':width, 'height':heigth}

sct = mss()

while True:
    begin_time = time()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('test', np.array(img_bgr))
    print('This frame takes {} seconds.'.format(time()-begin_time))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break




# from PIL import ImageGrab
# import numpy as np
# import cv2

# import autopy   

# wScr, hScr = autopy.screen.size()
# while(True):
#     img = ImageGrab.grab(bbox=(0,0,int(wScr),int(hScr))) #bbox specifies specific region (bbox= x,y,width,height)
#     img_np = np.array(img)
#     # frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("test", img_np)
#     cv2.waitKey(0)
#     if cv2.waitKey(0) & KeyboardInterrupt :
#         break
        
# cv2.destroyAllWindows()