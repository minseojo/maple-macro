import pyautogui
import keyboard
import time

time.sleep(2)
#im = pyautogui.screenshot(region=(0,0, 300, 400)) 지정 이미지 찍기

consumption_location = pyautogui.locateOnScreen('consumption.png', confidence=0.98) #소비창
re_location = pyautogui.locateOnScreen('re.png', confidence=0.99) # 한 번 더 하기
ad3_location = pyautogui.locateOnScreen('ad3.png', confidence=0.99) #공3퍼
ad6_location = pyautogui.locateOnScreen('ad6.png', confidence=0.99) #공6퍼

consumption_x=0 #소비
consumption_y=0

mouse_left=20
mouse_top=100

resize=-1 # 큐브 돌릴 여부 => 레어인 경우(resize==0)에만 돌림
want=-1
count=0

pyautogui.click(consumption_location)
cube_center = pyautogui.locateCenterOnScreen('cube.png', confidence=0.98)
pyautogui.doubleClick(cube_center)
pyautogui.doubleClick(mouse_left, mouse_top)

ad3_where = None
ad3_where2 = None
ad6_where = None
while 1:
    if keyboard.is_pressed('q'):
        print("끝")
        break
    epic_location =  pyautogui.locateOnScreen('epic.png', confidence=0.98)
    rare_location =  pyautogui.locateOnScreen('rare.png', confidence=0.98)

    if epic_location:
        resize=1
        print('에픽 달성')
        print(want)
        im1 = pyautogui.screenshot('im1.png', region=(320, 368, 167, 16)) #잠재 1줄
        im2 = pyautogui.screenshot('im2.png', region=(320, 382, 167, 16)) #잠재 2줄
        im3 = pyautogui.screenshot('im3.png', region=(320, 396, 167, 16)) #잠재 3줄
        ad3_where = pyautogui.locateOnScreen('ad3.png' , confidence=0.98)
        ad6_where = pyautogui.locateOnScreen('ad6.png' , confidence=0.98)
        bar_where = pyautogui.locateOnScreen('bar.png' , confidence=0.98)
        if want<1:
            while 1:
                re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
                
                want=0
                #if (pyautogui.locateOnScreen('ad3.png' , confidence=0.99, region=(320, 368, 167, 16)) or pyautogui.locateOnScreen('ad3.png' , confidence=0.99, region=(320, 382, 167, 16)) or pyautogui.locateOnScreen('ad3.png' , confidence=0.99, region=(320, 396, 167, 16))):
                 #       want+=1
                #if (pyautogui.locateOnScreen('ad6.png' , confidence=0.99, region=(320, 368, 167, 16)) or pyautogui.locateOnScreen('ad6.png' , confidence=0.99, region=(320, 382, 167, 16)) or pyautogui.locateOnScreen('ad6.png' , confidence=0.99, region=(320, 396, 167, 16))):
                       # want+=2
               # if (pyautogui.locateOnScreen('bar.png' , confidence=0.99, region=(320, 368, 167, 16)) or pyautogui.locateOnScreen('bar.png' , confidence=0.99, region=(320, 382, 167, 16)) orpyautogui.locateOnScreen('bar.png' , confidence=0.99, region=(320, 396, 167, 16))):
                       
                      # want+=1.5
                if ad6_where:
                    want+=2
                if ad3_where:
                    want+=1
                if bar_where:
                    want+=1
                print(want)        
                if want>=2:
                    time.sleep(1)
                    want=-1
                    ad3_where = None
                    ad6_where = None
                    bar_where = None
                    break
                pyautogui.click(re_center)
                pyautogui.press('enter') 
                pyautogui.press('enter')   
                pyautogui.press('enter')
                ad3_where = pyautogui.locateOnScreen('ad3.png' , confidence=0.98)
                ad6_where = pyautogui.locateOnScreen('ad6.png' , confidence=0.98)
                ad3_where2 = pyautogui.locateOnScreen('bar.png' , confidence=0.98)
                im1 = pyautogui.screenshot('im1.png', region=(320, 368, 167, 16)) #잠재 1줄
                im2 = pyautogui.screenshot('im2.png', region=(320, 382, 167, 16)) #잠재 2줄
                im3 = pyautogui.screenshot('im3.png', region=(320, 396, 167, 16)) #잠재 3줄
                
                time.sleep(0.3)
                if keyboard.is_pressed('q'):
                    print("끝")
                    exit()

        time.sleep(1)
        pyautogui.moveTo(470, 450)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click(consumption_location)
        time.sleep(1)
        pyautogui.doubleClick(20, 100)
        time.sleep(0.5)
        mouse_left+=44
        if count>=3:
            exit()
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
