
import pyautogui 
import time
import keyboard

while True:

    if keyboard.is_pressed('ctrl'):
        break

    time.sleep(0.1)
    pyautogui.moveTo(1920/2,5)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(600,600)




