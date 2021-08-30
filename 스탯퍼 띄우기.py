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
stat_str=0
stat_dex=0
stat_luk=0
stat_int=0
print(cube_count)
while 1:
    if cube_count>=2999:
        exit()
    if count>=2:
        exit()
    if keyboard.is_pressed('q'):
        print("끝")
        exit()
    epic_location =  pyautogui.locateOnScreen('epic.png', confidence=0.98)
    rare_location =  pyautogui.locateOnScreen('rare.png', confidence=0.98)

    if epic_location:
        if count>=2:
            exit()
        if cube_count>=2999:
            exit()
        resize=1
        print('에픽 달성')
        count+=1

        im1 = pyautogui.screenshot('im1.png', region=(320, 370, 167, 12)) #잠재 1줄
        im2 = pyautogui.screenshot('im2.png', region=(320, 379, 167, 12)) #잠재 2줄
        im3 = pyautogui.screenshot('im3.png', region=(320, 393, 167, 12)) #잠재 3줄

        if want<1:
            while 1:
                stat_str=0
                stat_dex=0
                stat_luk=0
                stat_int=0
                cube_count+=1
                if cube_count>=2999:
                    exit()
                re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
                want=0
                im1 = pyautogui.screenshot('im1.png', region=(320, 365, 160, 14)) #잠재 1줄
                im2 = pyautogui.screenshot('im2.png', region=(320, 379, 160, 14)) #잠재 2줄
                im3 = pyautogui.screenshot('im3.png', region=(320, 393, 160, 14)) #잠재 3줄
                for i in pyautogui.locateAllOnScreen('all3.png', confidence=0.92):
                     print('all3')
                     print(i.top)
                     if (i.top==367):
                         stat_str+=3
                         stat_dex+=3
                         stat_luk+=3
                         stat_int+=3
                         print('첫번째 줄 올탯3퍼')
                     else:
                         print(i.top)
                         print("올탯정보없음")
                        
                for i in pyautogui.locateAllOnScreen('str3.png', confidence=0.92):
                    if (i.top==381):
                        stat_str+=3
                        print('두번째 줄 힘3퍼')   
                    if (i.top==395):
                        stat_str+=3
                        print('세번째 줄 힘3퍼')
                    else:
                   #     stat_str+=3
                        print('str3')
                        print(i.top)
                        print('첫번째 줄 힘3퍼 정보없') 
                        
                for i in pyautogui.locateAllOnScreen('str6.png', confidence=0.93):
                    if (i.top==367):
                        stat_str+=6
                        print('첫번째 줄 힘6퍼')
                        
                    if (i.top==381):
                        stat_str+=6
                        print('두번째 줄 힘6퍼')
                    if (i.top==395):
                        stat_str+=6
                        print('str6')
                        print(i.top)                        
                        print('세번째 줄 힘6퍼')
                        
                for i in pyautogui.locateAllOnScreen('dex3.png', confidence=0.92):
                    if (i.top==381):
                        stat_dex+=3
                        print('두번째 줄 덱3퍼')
                    if (i.top==395):
                        stat_dex+=3
                        print('세번째 줄 덱3퍼')
                    else:
                        #stat_dex+=3
                        print('dex3')
                        print(i.top)
                        print('첫번째 줄 덱3퍼 정보없')
                        
                for i in pyautogui.locateAllOnScreen('dex6.png', confidence=0.97):
                    if (i.top==369):
                        stat_dex+=6
                        print('첫번째 줄 덱6퍼')
                    if (i.top==397):    
                        stat_dex+=6
                        print('세번째 줄 덱6퍼')
                    if(i.top==383 or i.top==384):
                        print(i.top)
                        print('두번째 줄 덱6퍼')
                        
                for i in pyautogui.locateAllOnScreen('luk3.png', confidence=0.90):
                    print('luk3')
                    print(i.top)
                    if (i.top==367):
                        stat_luk+=3
                        print('첫번째 줄 럭3퍼')
                    if (i.top==382):
                        stat_luk+=3
                        print('두번째 줄 럭3퍼')
                    if (i.top==396):
                        stat_luk+=3
                        print('세번째 줄 럭3퍼')
                        
                for i in pyautogui.locateAllOnScreen('luk6.png', confidence=0.92):
                    print('luk6')
                    print(i.top)
                    if (i.top==367):
                        stat_luk+=6
                        print('첫번째 줄 럭6퍼')
                    if (i.top==381 or i.top==382):
                        stat_luk+=6
                        print('두번째 줄 럭6퍼')
                    if(i.top==395 or i.top==396):
                        stat_luk+=6
                        print('세번째 줄 럭6퍼')
                        
                for i in pyautogui.locateAllOnScreen('int3.png', confidence=0.92):
                    print('int3')
                    print(i.top)
                    if (i.top==367):
                        stat_int+=3
                        print('첫번째 줄 인3퍼')
                    if (i.top==382):
                        stat_int+=3
                        print('두번째 줄 인3퍼')
                    if (i.top==396):
                        stat_int+=3
                        print('세번째 줄 인3퍼')
                        
                for i in pyautogui.locateAllOnScreen('int6.png', confidence=0.97):
                    print('int6')
                    
                    print(i.top)
                    if (i.top==369):
                        stat_int+=6
                        print('첫번째 줄 인트6퍼')
                    if (i.top==382):
                        stat_int+=6
                        print('두번째 줄 인트6퍼')
                    if (i.top==395 or i.top==396):
                        stat_int+=6
                        print('세번째 줄 인트6퍼')
                    
                print(stat_str)
                print(stat_dex)
                print(stat_luk)
                if stat_str>=12 or stat_dex>=12 or stat_luk>=12 or stat_int>=15:
                    print("완성")
                    stat_str=0
                    stat_dex=0
                    stat_luk=0
                    stat_int=0
                    exit()
                    if count>=2:
                        exit()
                    time.sleep(1)
                    break
                if count>=2:
                    exit()
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
        
    elif rare_location: 
        resize=0
        
    if resize!=1:
        cube_count+=1
        if count>=2:
            exit()
        if cube_count>=2999:
            exit()
        print(cube_count)
        re_center = pyautogui.locateCenterOnScreen('re.png', confidence=0.98)
        pyautogui.click(re_center)
        pyautogui.press('enter') 
        pyautogui.press('enter')
        pyautogui.press('enter')


    time.sleep(1.5)
