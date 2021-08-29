import pyautogui
import keyboard
import time

while 1:
    for i in pyautogui.locateAllOnScreen('ad3.png', confidence=0.96):
        print('ad3')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('ad6.png', confidence=0.96):
        print('ad6')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('bar.png', confidence=0.96):
        print('bar')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('str3.png', confidence=0.92):
        print('str3')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('str6.png', confidence=0.93):
        print('str6')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('dex3.png', confidence=0.92):
        print('dex3')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('dex6.png', confidence=0.97):
        print('dex6')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('luk3.png', confidence=0.93):
        print('luk3')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('luk6.png', confidence=0.96):
        print('luk6')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('int3.png', confidence=0.92):
        print('int3')
        print(i.top)
    for i in pyautogui.locateAllOnScreen('int6.png', confidence=0.97):
        print('int6')
        print(i.top)

