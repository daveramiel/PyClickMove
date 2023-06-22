import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    for i in range(10,98):
        pyautogui.click()
        time.sleep(120)