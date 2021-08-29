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

def xxx(value):
    if(367<=value.top<=369):
            print(value)
    if(381<=value.top<=383):
            print(value)
    if(395<=value.top<=397):
            print(value)
            
print(cube_count)
while 1:
    if cube_count>=3000:
        exit()
    if keyboard.is_pressed('q'):
        print("끝")
        exit()
    epic_location =  pyautogui.locateOnScreen('epic.png', confidence=0.98)
    rare_location =  pyautogui.locateOnScreen('rare.png', confidence=0.98)

    if epic_location:
        if cube_count>=3000:
            exit()
        resize=1
        print('에픽 달성')
        print(want)
        im1 = pyautogui.screenshot('im1.png', region=(320, 370, 167, 13)) #잠재 1줄
        im2 = pyautogui.screenshot('im2.png', region=(320, 383, 167, 13)) #잠재 2줄
        im3 = pyautogui.screenshot('im3.png', region=(320, 396, 167, 14)) #잠재 3줄

        if want<1:
            while 1:
                cube_count+=1
                if cube_count>=3000:
                    exit()
                re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
                want=0
                im1 = pyautogui.screenshot('im1.png', region=(320, 370, 160, 13)) #잠재 1줄
                im2 = pyautogui.screenshot('im2.png', region=(320, 383, 160, 13)) #잠재 2줄
                im3 = pyautogui.screenshot('im3.png', region=(320, 396, 160, 13)) #잠재 3줄
                ad3_where = pyautogui.locateOnScreen('ad3.png' ,confidence=0.96))
                ad3_where2 = pyautogui.locateOnScreen('ad3.png' , confidence=0.96)
                ad3_where3 = pyautogui.locateOnScreen('ad3.png' , confidence=0.96)
                
                ad6_where = pyautogui.locateOnScreen('ad6.png' , confidence=0.96)
                ad6_where2 = pyautogui.locateOnScreen('ad6.png' , confidence=0.96)
                ad6_where3 = pyautogui.locateOnScreen('ad6.png' , confidence=0.96)
                
                bar_where = pyautogui.locateOnScreen('bar.png' , confidence=0.96)
                
                str3_where = pyautogui.locateOnScreen('str3.png' , confidence=0.8)
                str6_where = pyautogui.locateOnScreen('str6.png' , confidence=0.8)
                dex3_where = pyautogui.locateOnScreen('dex3.png' , confidence=0.8)
                dex6_where = pyautogui.locateOnScreen('dex6.png' , confidence=0.8)
                luk3_where = pyautogui.locateOnScreen('luk3.png' , confidence=0.8)
                luk6_where = pyautogui.locateOnScreen('luk6.png' , confidence=0.8)                
                int3_where = pyautogui.locateOnScreen('int3.png' , confidence=0.8)
                int6_where = pyautogui.locateOnScreen('int6.png' , confidence=0.8)

                time.sleep(0.2)
                if(ad3_where):
                    xxx(str3_where)
                if(ad3_where):
                    xxx(str3_where)
                if(str3_where):
                    xxx(str3_where)


                if(str3_where):
                    xxx(str3_where)
                if(str6_where):
                    xxx(str6_where)
                if(dex3_where):
                    xxx(dex3_where)
                if(dex6_where):
                    xxx(dex6_where)
                if(luk3_where):
                    xxx(luk3_where)
                if(luk6_where):
                    xxx(luk6_where)
                if(int3_where):
                    xxx(int3_where)
                if(int6_where):
                    xxx(int6_where)
                        
                time.sleep(0.8)
                    
                print(want)        
                if want>=9:
                    want=-1
                    time.sleep(1)
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
        if count>=1:
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
        
    if resize!=1:
        cube_count+=1
        if cube_count>=3000:
            exit()
        print(cube_count)
        re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
        pyautogui.click(re_center)
        pyautogui.press('enter') 
        pyautogui.press('enter')
        pyautogui.press('enter')


    time.sleep(1.5)
