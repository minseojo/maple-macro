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
cube_count=0
pyautogui.click(consumption_location)
cube_center = pyautogui.locateCenterOnScreen('cube.png', confidence=0.98)
pyautogui.doubleClick(cube_center)
pyautogui.doubleClick(mouse_left, mouse_top)
cube_count+=1

ad3_where = None
ad6_where = None
bar_where = None
str3_where=None
str6_where=None
dex3_where=None
dex6_where=None
luk3_where=None
luk6_where=None
int3_where=None
int6_where=None
all3_where=None
all6_where=None
            
print(cube_count)
while 1:
    if cube_count>=3000:
        exit()
    if count>=4:
        exit()
    if keyboard.is_pressed('q'):
        print("끝")
        exit()
    epic_location =  pyautogui.locateOnScreen('epic.png', confidence=0.98)
    rare_location =  pyautogui.locateOnScreen('rare.png', confidence=0.98)

    if epic_location:
        if count>=4:
            exit()
        if cube_count>=3000:
            exit()
        resize=1
        print('에픽 달성')
        count+=1
        print(want)
        im1 = pyautogui.screenshot('im1.png', region=(320, 370, 167, 12)) #잠재 1줄
        im2 = pyautogui.screenshot('im2.png', region=(320, 379, 167, 12)) #잠재 2줄
        im3 = pyautogui.screenshot('im3.png', region=(320, 393, 167, 12)) #잠재 3줄

        if want<1:
            while 1:
                if count>=4:
                    exit()
                cube_count+=1
                if cube_count>=500:
                    exit()
                re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
                want=0
                im1 = pyautogui.screenshot('im1.png', region=(320, 365, 160, 14)) #잠재 1줄
                im2 = pyautogui.screenshot('im2.png', region=(320, 379, 160, 14)) #잠재 2줄
                im3 = pyautogui.screenshot('im3.png', region=(320, 393, 160, 14)) #잠재 3줄
                for i in pyautogui.locateAllOnScreen('ad3.png', confidence=0.96):
                    if (i.top==367):
                        print('첫번째 줄 공3퍼')
                        want+=3
                    if (i.top==381):
                        print('두번째 줄 공3퍼')
                        want+=3
                    if (i.top==395):
                        print('세번째 줄 공3퍼')
                        want+=3
                        
                for i in pyautogui.locateAllOnScreen('ad6.png', confidence=0.96):
                    if (i.top==368):
                        print('첫번째 줄 공6퍼')
                        want+=6
                    if (i.top==382):
                        print('두번째 줄 공6퍼')
                        want+=6
                    if (i.top==396):
                        print('세번째 줄 공6퍼')
                        want+=6
                        
                for i in pyautogui.locateAllOnScreen('bar.png', confidence=0.97):
                    if (i.top==369):
                        print('첫번째 줄 방무15퍼')
                        want+=3
                    if (i.top==383):
                        print('두번째 줄 방무15퍼')
                        want+=3
                    if (i.top==397):
                        print('세번째 줄 방무15퍼')
                        want+=3

                time.sleep(0.8)
                    
                print(want)        
                if want>=9:
                    want=-1
                    time.sleep(1)
                    exit()
                    ad3_where = None
                    ad6_where = None
                    bar_where = None
                    break
                pyautogui.click(re_center)
                pyautogui.press('enter') 
                pyautogui.press('enter')   
                pyautogui.press('enter')
                print(cube_count)
                time.sleep(1)
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
        
        pyautogui.moveTo(mouse_left, mouse_top)
        pyautogui.click()
        resize=0
        count+=1
        
    elif rare_location: 
        resize=0
        
    if resize!=1:
        cube_count+=1
        if count>=4:
            exit()
        if cube_count>=3000:
            exit()
        print(cube_count)
        re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
        pyautogui.click(re_center)
        pyautogui.press('enter') 
        pyautogui.press('enter')
        pyautogui.press('enter')


    time.sleep(1.5)
