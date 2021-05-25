from typing import Mapping
import pyautogui
import time
time.sleep(3)
text = "text"
for _ in range(0,80):
 pyautogui.typewrite(text)
 pyautogui.press('enter')