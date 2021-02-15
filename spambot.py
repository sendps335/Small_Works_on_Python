import pyautogui
import time
time.sleep(5)
f=open(r'C:\Users\DEBIPRASAD\Documents\CID Episodes.rtf','r')
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press("enter")
    