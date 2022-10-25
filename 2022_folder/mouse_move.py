#!/usr/bin/python3 
print("************************************************")
print ("mouse motion")
print("************************************************\n")

import pyautogui
import time

while True:
    a, b = pyautogui.position()
    time.sleep(60)
    c, d = pyautogui.position()
    if a == c  :
       x = a + 500
       y = b + 500
       pyautogui.moveTo(x, y, 0.5)
       pyautogui.moveTo(a, b, 0.5)
       print('Moved')
    else : print (' mouse moved by user')
    print('one cycle finished')
