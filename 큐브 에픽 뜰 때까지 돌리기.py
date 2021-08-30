import pyautogui
import keyboard
import time

time.sleep(2)
#im = pyautogui.screenshot(region=(0,0, 300, 400)) 지정 이미지 찍기

consumption_location = pyautogui.locateOnScreen('consumption.png', confidence=0.98) #소비창
re_location = pyautogui.locateOnScreen('re.png', confidence=0.98) # 한 번 더 하기
ad3_location = pyautogui.locateOnScreen('ad3.png', confidence=0.98) #공3퍼
ad6_location = pyautogui.locateOnScreen('ad6.png', confidence=0.98) #공6퍼
consumption_x=0 #소비
consumption_y=0

mouse_left=20
mouse_top=100

resize=-1 # 큐브 돌릴 여부 => 레어인 경우(resize==0)에만 돌림
count=0
cube_count=0
pyautogui.click(consumption_location)
cube_center = pyautogui.locateCenterOnScreen('cube.png', confidence=0.98)
pyautogui.doubleClick(cube_center)
pyautogui.doubleClick(mouse_left, mouse_top)

while 1:
    if count==4 or cube_count>=2999:
        exit()
    epic_location =  pyautogui.locateOnScreen('epic.png', confidence=0.98)
    rare_location =  pyautogui.locateOnScreen('rare.png', confidence=0.98)
        
    if epic_location:
        resize=1
        print('에픽 달성')
        count+=1
        if count==4 or cube_count>=2999:
            exit()
            count=0
            mouse_left=20
            mouse_top+=44
            time.sleep(0.5)
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
        pyautogui.moveTo(mouse_left, mouse_top)
        pyautogui.click()
        resize=0
        
    elif rare_location: 
        resize=0
        print('레어')
        
    if resize!=1:
        if count==4 or cube_count>=2999:
            exit()
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
