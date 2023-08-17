import pyautogui
import keyboard
import time
import pytesseract
import numpy as np
import cv2
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer


# 메이플 화면 맨 왼쪽위로 고정
def scree_fix():
    title = pyautogui.locateCenterOnScreen('images/start.PNG', confidence=0.7, grayscale=True)
    pyautogui.moveTo(title)
    pyautogui.mouseDown()
    pyautogui.moveTo(50, 15)
    pyautogui.mouseUp()

    time.sleep(0.3)
    item_inven = pyautogui.locateCenterOnScreen('images/item_inven_0.PNG', confidence=0.9, grayscale=True)
    # 인벤토리창 열기
    if (item_inven is None):
        pyautogui.click(880, 770)
        time.sleep(0.3)
        pyautogui.click(880, 680)

    time.sleep(0.5)

    # 인벤토리 옮기기
    item_inven = pyautogui.locateCenterOnScreen('images/item_inven_0.PNG', confidence=0.9, grayscale=True)
    cursor = pyautogui.moveTo(item_inven)
    pyautogui.mouseDown()
    pyautogui.moveTo(350, 50)
    pyautogui.mouseUp()

    time.sleep(0.2)

INF = 999
# 뽑고 싶은 큐브 옵션
stat_name = ["STR", "DEX", "INT", "LUK", "AD", "AP", "DAMAGE", "BAR", "HP"]
want_stat = [INF, INF, INF, INF, INF, INF, INF, INF, INF]
STR = int(0)
DEX = int(1)
INT = int(2)
LUK = int(3)
AD =int(4)
AP = int(5)
DAMAGE = int(6)
BAR = int(7)
HP = int(8)

# 현재 큐브 옵션 값
stat =  [0, 0, 0, 0, 0, 0, 0, 0, 0]

# 큐재 큐브 옵션 설정
def add_stat(name, value):
    if (value == 1):
        value = 3
    if (value == 2):
        value = 6

    stat[name] += value
    print(stat_name[name] + str(stat[name]))
    
# 큐브 스탯 옵션 전처리
def cube_check():
    cube_grade =  pyautogui.screenshot('images/potential/cube_grade.PNG', region=(665, 442, 40, 15))
    potential_1 = pyautogui.screenshot('images/potential/potential_1.PNG', region=(605, 456, 160, 15))
    potential_2 = pyautogui.screenshot('images/potential/potential_2.PNG', region=(605, 470, 160, 15))
    potential_3 = pyautogui.screenshot('images/potential/potential_3.PNG',  region=(605, 484, 160, 15))
    time.sleep(0.1)
    res = False
    for i in range (0, 3):
        img_path = "images/potential/potential_" + str(i+1) + ".PNG"
        img = cv2.imread(img_path)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        text = pytesseract.image_to_string(img_path, lang = 'kor+eng')
        hsv_text = pytesseract.image_to_string(hsv, lang = 'kor+eng')

        if (text == "내: +2%\n"):
            add_stat(LUK, 2)
            
        if (len(text) != 0 and text.strip()[-1] == '%'):
            name = text[:4]
            value = int(text.strip()[-2:-1])
            if (name == "STR:" or name == "STR "):
                add_stat(STR, value)
            if (name == "DEX:" or name == "DEX "):
                add_stat(DEX, value)
            if (name == "INT:" or name == "INT "):
                add_stat(INT, value)
            if (name == "LUK:" or name == "LUK "):
                add_stat(LUK, value)
            if (name == "마력 :"):
                add_stat(AP, value)
            if (name == "데미지 "):
                add_stat(DAMAGE, value)
            if (name == "최대 H"):
                add_stat(HP, value)
 
        # 올스탯 3%
        if (text == "때\nI\nif\n\n+3%\n"):
            add_stat(STR, 3)
            add_stat(DEX, 3)
            add_stat(INT, 3)
            add_stat(LUK, 3)

        if (text == "때\nI\nif\n\n+1%\n"):
            add_stat(STR, 1)
            add_stat(DEX, 1)
            add_stat(INT, 1)
            add_stat(LUK, 1)

        # 공격력 
        if (hsv_text == "공격력 49%:\n" or hsv_text == "Reet +8%:\n" or text =="공격력 49%:\n" or text == "Reet +8%:\n"):
            add_stat(AD, 3)
                
        if (hsv_text == "공격력 : 6%-\n" or text == "공격력 : 6%-\n"):
            add_stat(AD, 6)


    for i in range(0, 9):
        if (stat[i] >= want_stat[i]):
            res = True
        stat[i] = 0
        
    if (res == True): return True
    else: return False




# 장비창 디폴트 좌표
default_x = 30
default_y = 100
# 만들 아이템 좌표 x, y
x = default_x
y = default_y
number_of_items_to_make = 0 # 만들 아이템 개수
number_of_items_maked = 0 # 현재 만든 아이템 개수


# 큐브 디폴트, 현재 사용하는 큐브 좌표
cube_default_x = 30
cube_default_y = 100
cube_x = cube_default_x
cube_y = cube_default_y
number_of_cubes_to_use = 0 # 사용 할 큐브 개수
number_of_cubes_used = 0 # 현재 사용한 큐브 개수


# 큐브 인벤위치 변경
def cube_location():
    global cube_x
    global cube_y
    global cube_default_x
    if (number_of_cubes_used != 0 and number_of_cubes_used % 3000 == 0):
        cube_x += 42
 
    elif (number_of_cubes_used != 0 and number_of_cubes_used % 12000 == 0):
        cube_y += 42
        cube_x = cube_default_x

    elif (number_of_cubes_used != 0 and number_of_cubes_used % 96000 == 0):
        cube_default_x = (30 + 42 * 4 * ((number_of_cubes_used) / 96000))
        cube_y = cube_default_y
        cube_x = cube_default_x


# 큐브 한번더 누르기
def cube_reRoll():
    pyautogui.click(650, 535) # 한번더 누르기
    pyautogui.press('enter', 3)

# 큐브 확인 누르기
def cube_ok():
    pyautogui.click(750, 535) # 확인  누르기
                
        
def start():
    scree_fix()
    global default_x
    global default_y
    global x
    global y
    global number_of_items_to_make
    global number_of_items_maked

    global cube_default_x
    global cube_default_y
    global cube_x
    global cube_y
    global number_of_cubes_to_use
    global number_of_cubes_used

    while(number_of_items_maked < number_of_items_to_make
          and number_of_cubes_used < number_of_cubes_to_use):
        for i in range(0, 4):
            check = False
            number_of_cubes_used += 1
            if (number_of_cubes_used != 0 and number_of_cubes_used % 3000 == 0):
                cube_location()
            item_consumption = pyautogui.click(51, 65) # 소비창 클릭
            time.sleep(0.1)
            pyautogui.doubleClick(cube_x, cube_y)# 수큐 더블클릭
            pyautogui.click(x, y)
            pyautogui.press('enter', 2)
            time.sleep(1.5)
            check = cube_check()
            time.sleep(0.2)
            
            while (number_of_cubes_used < number_of_cubes_to_use):
                number_of_cubes_used += 1
                if (number_of_cubes_used != 0 and number_of_cubes_used % 3000 == 0):
                    cube_location()
                time.sleep(0.2)
                if (check == True):
                    number_of_items_maked += 1
                    cube_ok()
                    break
                else:
                    cube_reRoll()
                    time.sleep(1.5)
                    check = cube_check()
            if (number_of_items_maked >= number_of_items_to_make):
                break
            if (number_of_cubes_used >= number_of_cubes_to_use):
                break
            
            x += 42
            
        y += 42
        x = default_x
        if (number_of_items_maked % 32 == 0):
            default_x = (30 + 42 * 4 * ((number_of_items_maked) / 32))
            y = default_y
            x = default_x
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스탯
        self.lbl = QLabel('스탯 설정', self)
        self.lbl.move(60, 25)
        
        #str
        self.lbl = QLabel('STR', self)
        self.lbl.move(50, 55)
        cb_str = QComboBox(self)
        cb_str.addItem('∞%')
        cb_str.addItem('3%')
        cb_str.addItem('6%')
        cb_str.addItem('9%')
        cb_str.addItem('12%')
        cb_str.addItem('15%')
        cb_str.addItem('18%')
        cb_str.move(85, 50)

        #dex
        self.lbl = QLabel('DEX', self)
        self.lbl.move(50, 85)
        cb_dex = QComboBox(self)
        cb_dex.addItem('∞%')
        cb_dex.addItem('3%')
        cb_dex.addItem('6%')
        cb_dex.addItem('9%')
        cb_dex.addItem('12%')
        cb_dex.addItem('15%')
        cb_dex.addItem('18%')
        cb_dex.move(85, 80)

        #int
        self.lbl = QLabel('INT', self)
        self.lbl.move(50, 115)
        cb_int = QComboBox(self)
        cb_int.addItem('∞%')
        cb_int.addItem('3%')
        cb_int.addItem('6%')
        cb_int.addItem('9%')
        cb_int.addItem('12%')
        cb_int.addItem('15%')
        cb_int.addItem('18%')
        cb_int.move(85, 110)

        #LUK
        self.lbl = QLabel('LUK', self)
        self.lbl.move(50, 145)
        cb_luk = QComboBox(self)
        cb_luk.addItem('∞%')
        cb_luk.addItem('3%')
        cb_luk.addItem('6%')
        cb_luk.addItem('9%')
        cb_luk.addItem('12%')
        cb_luk.addItem('15%')
        cb_luk.addItem('18%')
        cb_luk.move(85, 140)

        #HP
        self.lbl = QLabel('HP', self)
        self.lbl.move(50, 175)
        cb_hp = QComboBox(self)
        cb_hp.addItem('∞%')
        cb_hp.addItem('3%')
        cb_hp.addItem('6%')
        cb_hp.addItem('9%')
        cb_hp.addItem('12%')
        cb_hp.addItem('15%')
        cb_hp.addItem('18%')
        cb_hp.move(85, 170)
        
        #무기
        self.lbl = QLabel('무기 설정', self)
        self.lbl.move(200, 25)
        
        #ad
        self.lbl = QLabel('공격력', self)
        self.lbl.move(190, 55)
        cb_ad = QComboBox(self)
        cb_ad.addItem('∞%')
        cb_ad.addItem('3%')
        cb_ad.addItem('6%')
        cb_ad.addItem('9%')
        cb_ad.addItem('12%')
        cb_ad.addItem('15%')
        cb_ad.addItem('18%')
        cb_ad.move(235, 50)

        #ap
        self.lbl = QLabel('   마력', self)
        self.lbl.move(190, 85)
        cb_ap = QComboBox(self)
        cb_ap.addItem('∞%')
        cb_ap.addItem('3%')
        cb_ap.addItem('6%')
        cb_ap.addItem('9%')
        cb_ap.addItem('12%')
        cb_ap.addItem('15%')
        cb_ap.addItem('18%')
        cb_ap.move(235, 80)

        #damage
        self.lbl = QLabel('데미지', self)
        self.lbl.move(190, 115)
        cb_damage = QComboBox(self)
        cb_damage.addItem('∞%')
        cb_damage.addItem('3%')
        cb_damage.addItem('6%')
        cb_damage.addItem('9%')
        cb_damage.addItem('12%')
        cb_damage.addItem('15%')
        cb_damage.addItem('18%')
        cb_damage.move(235, 110)

        # 스탯설정
        cb_str.activated[str].connect(lambda text: self.onActivated(text, 'STR'))
        cb_dex.activated[str].connect(lambda text: self.onActivated(text, 'DEX'))
        cb_int.activated[str].connect(lambda text: self.onActivated(text, 'INT'))
        cb_luk.activated[str].connect(lambda text: self.onActivated(text, 'LUK'))
        cb_ad.activated[str].connect(lambda text: self.onActivated(text, 'AD'))
        cb_ap.activated[str].connect(lambda text: self.onActivated(text, 'AP'))
        cb_damage.activated[str].connect(lambda text: self.onActivated(text, 'DAMAGE'))
        cb_hp.activated[str].connect(lambda text: self.onActivated(text, 'HP'))
        
        #필수설정
        self.lbl = QLabel('필수 설정', self)
        self.lbl.setStyleSheet("Color : red") #글자색 변환
        self.lbl.move(350, 25)

        #설정 할 아이템 개수
        self.lbl = QLabel('설정 할 아이템 개수', self)
        self.lbl.move(320, 55)
        
        cb_item = QComboBox(self)
        cb_item.addItem('0')
        for i in range (1, 129):
            cb_item.addItem(str(i))
        cb_item.move(435, 50)

        #수상한 큐브 개수
        self.lbl = QLabel('수상한 큐브 개수', self)
        self.lbl.move(325, 85)

        cb_cube = QComboBox(self)
        cb_cube.addItem("0개")
        cb_cube.addItem("10")
        cb_cube.addItem("50")
        cb_cube.addItem("100")
        cb_cube.addItem("300")
        cb_cube.addItem("500")
        cb_cube.addItem("1000")
        cb_cube.addItem("2000")
        for i in range(3000, 96001, 3000):
            cb_cube.addItem(str(i))
        cb_cube.move(424, 80)

        cb_item.activated[str].connect(lambda text: self.onActivated2(text, 'item'))
        cb_cube.activated[str].connect(lambda text: self.onActivated2(text, 'cube'))

        #시작
        self.start_btn = QPushButton('시작', self)
        self.start_btn.move(320 ,110)
        self.start_btn.clicked.connect(self.start_btn_click)
        #종료
        self.end_btn = QPushButton('종료', self)
        self.end_btn.move(410 ,110)
        self.end_btn.clicked.connect(self.close)
        
        self.setWindowTitle('수큐 매크로')
        self.setGeometry(1400, 200, 530, 230)
        self.show()
        self.setFixedSize(530, 230)
        
    def onActivated(self, text, option):
        idx = -1
        value = ' '
        
        if(text == "∞" or text == "∞%") :
            value = "999" #INF   
        elif (len(text) == 2):
            value = text[0]
        elif (len(text) == 3):
            value = text[0:2]
            
        for i in range (0, 9):
            if (stat_name[i] == option):
                idx = i
                break
        want_stat[idx] = int(value)

    def onActivated2(self, text, option):
        print(option + str(int(text)))
        global number_of_items_to_make
        global number_of_cubes_to_use
        if (option == "item"):
            number_of_items_to_make = int(text)
        if (option == "cube"):
            number_of_cubes_to_use = int(text)
        
    def start_btn_click(self):
        global number_of_items_maked
        number_of_items_maked = 0
        global number_of_cubes_used
        number_of_cubes_used = 0
        global default_x
        default_x = 30
        global default_y
        default_y = 100
        global x
        x = default_x
        global y
        y = default_y
        global cube_default_x
        cube_default_x = 30
        global cube_default_y
        cube_default_y = 100
        global cube_x
        cube_x = cube_default_x
        global cube_y
        cube_y = cube_default_y
        start()
        
    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        # sys.exit(1)

    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook


    #def cleanup(self):
        # 정리 작업을 수행하는 코드를 여기에 추가하세요.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyApp()
    widget.show()
    #app.aboutToQuit.connect(widget.cleanup)  # 종료 직전에 cleanup() 함수 호출
    app.exec_()
#768 : 1366
