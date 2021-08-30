import pyautogui
import time
import keyboard
from random import *

sign=0
xsize=0
ysize=0
while 1:
    if sign==0:
        sign=1
        time.sleep(2)
    xsize=300
    ysize=440
    ysize+= randint(1,10)
    xsize+= randint(50,100)
    pyautogui.doubleClick(x=xsize,y=ysize)
    pyautogui.press('enter')
    pyautogui.press('enter') 
    pyautogui.press('enter')
    pyautogui.doubleClick(x=xsize,y=ysize-50)
    time.sleep(1.5)
    if keyboard.is_pressed('q'):
        print("끝")
        break
