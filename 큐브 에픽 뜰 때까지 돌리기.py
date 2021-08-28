import pyautogui
import keyboard
import time

time.sleep(2)
#im = pyautogui.screenshot(region=(0,0, 300, 400)) 지정 이미지 찍기

consumption_location = pyautogui.locateOnScreen('consumption.png', confidence=0.98)
ok_location = pyautogui.locateOnScreen('ok.png', confidence=0.98)
re_location = pyautogui.locateOnScreen('re.png', confidence=0.98) # 한 번 더 하기

consumption_x=0 #소비
consumption_y=0

mouse_left=20
mouse_top=100

resize=-1 # 큐브 돌릴 여부 => 레어인 경우(resize==0)에만 돌림
count=0




pyautogui.click(consumption_location)
cube_center = pyautogui.locateCenterOnScreen('cube.png', confidence=0.98)
pyautogui.doubleClick(cube_center)
pyautogui.doubleClick(mouse_left, mouse_top)

while 1:
    epic_location =  pyautogui.locateOnScreen('epic.png', confidence=0.98)
    rare_location =  pyautogui.locateOnScreen('rare.png', confidence=0.98)
        
    if epic_location:
        resize=1
        print('에픽 달성')
        re_location = pyautogui.locateOnScreen('re.png', confidence=0.98) # 한 번 더 하기
        pyautogui.moveTo(470, 450)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click(consumption_location)
        time.sleep(0.5)
        #cube_center = pyautogui.locateCenterOnScreen('cube.png', confidence=0.98)
        pyautogui.doubleClick(20, 100)
        time.sleep(0.5)
        mouse_left+=44
        if count==7:
            count=0
            mouse_left=20
            mouse_top+=44
            time.sleep(0.5)
        pyautogui.moveTo(mouse_left, mouse_top)
        pyautogui.click()
        resize=0
        count+=1
        
    elif rare_location: 
        resize=0
        print('레어')
        
    if resize!=1:
        print('한 번 더 사용하기')
        re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
        pyautogui.click(re_center)
        pyautogui.press('enter') 
        pyautogui.press('enter')
        pyautogui.press('enter')


    time.sleep(1.5)
    
    if keyboard.is_pressed('q'):
        print("끝")
        break
