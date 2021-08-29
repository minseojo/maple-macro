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

check1=0
check2=0
check3=0
def xxx(value):
    check1=0
    check2=0
    check3=0
    if(367<=value.top<=369 and check1==0):
        check1=1
        print(value)
    if(381<=value.top<=383 and check2==0):
        check2=1
        print(value)
        time.sleep(0.1)
    if(395<=value.top<=397 and check3==0):
        check3=1
        print(value)
        time.sleep(0.1)

    check1=0
    check2=0
    check3=0
            
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
        im1 = pyautogui.screenshot('im1.png', region=(320, 370, 167, 12)) #잠재 1줄
        im2 = pyautogui.screenshot('im2.png', region=(320, 379, 167, 12)) #잠재 2줄
        im3 = pyautogui.screenshot('im3.png', region=(320, 393, 167, 12)) #잠재 3줄

        if want<1:
            while 1:
                cube_count+=1
                if cube_count>=3000:
                    exit()
                re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
                want=0
                im1 = pyautogui.screenshot('im1.png', region=(320, 365, 160, 14)) #잠재 1줄
                im2 = pyautogui.screenshot('im2.png', region=(320, 379, 160, 14)) #잠재 2줄
                im3 = pyautogui.screenshot('im3.png', region=(320, 393, 160, 14)) #잠재 3줄
                ad3_where = pyautogui.locateOnScreen('ad3.png' , confidence=0.96)
                ad6_where = pyautogui.locateOnScreen('ad6.png' , confidence=0.96)
                bar_where = pyautogui.locateOnScreen('bar.png' , confidence=0.96)
                str3_where = pyautogui.locateOnScreen('str3.png' , confidence=0.85)
                str6_where = pyautogui.locateOnScreen('str6.png' , confidence=0.97)
                dex3_where = pyautogui.locateOnScreen('dex3.png' , confidence=0.92)
                dex6_where = pyautogui.locateOnScreen('dex6.png' , confidence=0.97)
                luk3_where = pyautogui.locateOnScreen('luk3.png' , confidence=0.92)
                luk6_where = pyautogui.locateOnScreen('luk6.png' , confidence=0.97)                
                int3_where = pyautogui.locateOnScreen('int3.png' , confidence=0.99)
                int6_where = pyautogui.locateOnScreen('int6.png' , confidence=0.99)
                time.sleep(0.1)
                for i in pyautogui.locateAllOnScreen('ad3.png', confidence=0.96):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('ad6.png', confidence=0.96):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('bar.png', confidence=0.96):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('str3.png', confidence=0.82):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('str6.png', confidence=0.97):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('dex3.png', confidence=0.92):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('dex6.png', confidence=0.97):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('luk3.png', confidence=0.92):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('luk6.png', confidence=0.97):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('int3.png', confidence=0.92):
                    print(i.top)
                for i in pyautogui.locateAllOnScreen('int6.png', confidence=0.97):
                    print(i.top)
                    
                if (ad6_where):
                    if (ad6_where.top<=368 and check1==0):
                        check1=1
                        print('첫번째 줄 공6퍼')
                        print(ad6_where.top)   
                        want+=6
                        time.sleep(0.1)
                    if (379<=ad6_where.top<395 and check2==0):
                        check2=1
                        print('두번째 줄 공6퍼')
                        print(ad6_where.top)   
                        want+=6
                        time.sleep(0.1)
                    if (395<=ad6_where.top<407 and check3==0):
                        check3=1
                        print('세번째 줄 공6퍼')
                        print(ad6_where.top)   
                        want+=6
                        time.sleep(0.1)

                     
                if (ad3_where):
                    if (379<=ad3_where.top<=382 and check2==0):
                        check2=1
                        print('두번째 줄 공3퍼')
                        print(ad3_where.top)
                        want+=3
                        time.sleep(0.1)
                    if (395<=ad3_where.top<=397 and check3==0):
                        check3=1
                        print('세번째 줄 공3퍼')
                        print(ad3_where.top)
                        want+=3
                        time.sleep(0.1)
                    
                    
                if (bar_where):
                    if(bar_where.top==369):
                        print('첫번째 줄 방무')
                        print(bar_where.top)
                        want+=5
                        time.sleep(0.1)
                    if(bar_where.top==383):
                        print('두번째 줄 방무')
                        print(bar_where.top)
                        want+=5
                        time.sleep(0.1)
                    if(bar_where.top==397):
                        print('세번째 줄 방무')
                        print(bar_where.top)
                        want+=5
                        time.sleep(0.1)

                if(str3_where):
                    print('str3')
                    xxx(str3_where)
                if(str6_where):
                    print('str6')
                    xxx(str6_where)
                if(dex3_where):
                    print('dex3')
                    xxx(dex3_where)
                if(dex6_where):
                    print('dex6')
                    xxx(dex6_where)
                if(luk3_where):
                    print('luk3')
                    xxx(luk3_where)
                if(luk6_where):
                    print('luk6')
                    xxx(luk6_where)
                if(int3_where):
                    print('int3')
                    xxx(int3_where)
                if(int6_where):
                    print('int6')
                    xxx(int6_where)
                check1=0
                check2=0
                check3=0
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
