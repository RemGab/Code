import keyboard
import pyautogui
import cv2
import numpy as np
import pyautogui as pg
import time
path = r'Teams\Resources'

def detect_fleche_li():
    print('ça lance')
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    for pawn in pg.locateOnScreen(path + '\fleche.jpg', confidence=0.6):
        try:
            print(' c try')
            pg.moveTo(pawn)
            pg.click()
            break
        except:
            print(' c except')

            pass
    print('c rien')


def croix_outl():
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    for pawn in pg.locateAllOnScreen(path + '\close_outl.jpg', confidence=0.8):
        try:
            pg.moveTo(pawn)
            pg.click()
            break
        except:
            pass

def lecture_immersive():
    # print('LI')
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    for pawn in pg.locateAllOnScreen(path + '\li.jpg', confidence=0.8):
        try:
            detect_fleche_li()
            print("Commande effectuée")
        except:
            pass

def detect_book():
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    for pawn in pg.locateAllOnScreen(path + '\play.jpg', confidence=0.8):
        try:
            detect_fleche_li()
            print("Commande effectuée")
        except:
            pass

def outlook():
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    for pawn in pg.locateAllOnScreen(path + '\outl.jpg', confidence=0.99):
        try:
            croix_outl()
            time.sleep(2)
            keyboard.press('ENTER')
            print("Commande effectuée")

        except:
            pass

def suppr_detection():
    import cv2
    import numpy as np
    import pyautogui as pg
    import time
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    for pawn in pg.locateAllOnScreen(path + '\suppr.jpg', confidence=0.8):
        while True:
            try:
                pg.moveTo(pawn)
                time.sleep(0.01)
                pg.click()
                break
            except:
                pass

def message_detection():
    import cv2
    import pyautogui as pg
    import time
    counter = 0.3
    screenshot = pg.screenshot(
        path + '\ss.jpg')
    image = cv2.imread(
        path + '\ss.jpg')
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    image_copy = image.copy()

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w > 50 and h > 25 and y > 100 and x+w > 1700 and w != 369 and h != 53 and h != 54 and w != 371:
            cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 3)
            pg.moveTo(1850, 560)
            time.sleep(0.01)
            pg.click()
            pg.moveTo(x+w-5, y+h/2)
            while True:
                try:
                    i = 0
                    while i != 2:
                        pg.rightClick()
                        i += 1
                    break
                except:
                    pass
            # time.sleep(0)
            suppr_detection()
            # time.sleep(counter)
            pg.moveRel(x+w+10, 0)
            # time.sleep(counter)
    pg.moveTo(1920/2, 1020/2)


def open_win():
    import win32gui
    import win32com.client
    import pyautogui as pg
    import win32con
    import time
    chaine = "Microsoft Teams"
    banned = "Notification"
    def windowEnumerationHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    if __name__ == "__main__":
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if chaine.lower() in i[1].lower():
                if not banned.lower() in i[1].lower():
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.SendKeys('%')
                    win32gui.SetForegroundWindow(i[0])
                    win32gui.ShowWindow(i[0], 9)
                    win32gui.MoveWindow(i[0], -7, 0, 1920, 1920, True)
                    break
    # time.sleep(0)

def transition():
    import pyautogui as pg
    import time
    pg.moveTo(3*1920/4, 1020/2)
    pg.click
    s = 500
    pg.scroll(s)
    pg.scroll(-s)
    pg.scroll(s)
    time.sleep(0.1)


i = 0
while True:
    try:
        if i == 3:
            lecture_immersive()
            detect_book()
            outlook()
            i = 0
        if keyboard.is_pressed('right'):
            break
        if keyboard.is_pressed('right'):
            break
        open_win()
        if keyboard.is_pressed('right'):
            break
        message_detection()
        if keyboard.is_pressed('right'):
            break
        open_win()
        if keyboard.is_pressed('right'):
            break
        message_detection()
        if keyboard.is_pressed('right'):
            break
        transition()
        if keyboard.is_pressed('right'):
            break
        i += 1
        # print(i)
    except:
        pass
