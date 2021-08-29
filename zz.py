import pyautogui

img_capture = pyautogui.locateOnScreen("ad3.png", region=(1800, 0, 1920, 100))

pyautogui.moveTo(img_capture)
