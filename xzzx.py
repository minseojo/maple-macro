import pyautogui
button7location = pyautogui.locateOnScreen('luk6.png', confidence=0.95)
print(button7location.top)
