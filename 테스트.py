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
        
                for i in pyautogui.locateAllOnScreen('damage3.png', confidence=0.92):
                    print('damage3')
                    print(i.top)
                    if (i.top==367):
                        print('첫번째 줄 데미지3퍼')
                    if (i.top==381):
                        print('두번째 줄 데미지3퍼')
                    if (i.top==395):
                        print('세번째 줄 데미지3퍼')
                        
                for i in pyautogui.locateAllOnScreen('damage6.png', confidence=0.96):
                    print('damage6')
                    print(i.top)
                    if (i.top==367):
                        print('첫번째 줄 데미지6퍼')
                    if (i.top==381):
                        print('두번째 줄 데미지6퍼')
                    if (i.top==395):
                        print('세번째 줄 데미지6퍼')

                for i in pyautogui.locateAllOnScreen('all3.png', confidence=0.92):
                     print('all3')
                     print(i.top)
                     if (i.top!=381 and i.top!=395):
                         print('첫번째 줄 올탯3퍼')         
                     if (i.top==381):    
                         print('두번째 줄 올탯3퍼')   
                     if (i.top==395):
                         print('세번째 줄 올탯3퍼')
                        
                for i in pyautogui.locateAllOnScreen('str3.png', confidence=0.92):
                    print('str3')
                    print(i.top)
                    if (i.top!=381 and i.top!=395):
                        print('첫번째 줄 힘3퍼')         
                    if (i.top==381):    
                        print('두번째 줄 힘3퍼')   
                    if (i.top==395):
                        print('세번째 줄 힘3퍼')
                        
                for i in pyautogui.locateAllOnScreen('str6.png', confidence=0.93):
                    print('str6')
                    print(i.top)
                    if (i.top==367):
                        print('첫번째 줄 힘6퍼')
                    if (i.top==381):
                        print('두번째 줄 힘6퍼')
                    if (i.top!=367 and i.top!=381):
                        print('세번째 줄 힘6퍼')
                        
                for i in pyautogui.locateAllOnScreen('dex3.png', confidence=0.92):
                    print('dex3')
                    print(i.top)
                    if (i.top!=381 and i.top!=395):
                        print('첫번째 줄 덱3퍼')
                    if (i.top==381):
                        print('두번째 줄 덱3퍼')
                    if (i.top==395):
                        print('세번째 줄 덱3퍼')
                        
                for i in pyautogui.locateAllOnScreen('dex6.png', confidence=0.97):
                    print('dex6')
                    print(i.top)
                    if (i.top==369):
                        print('첫번째 줄 덱6퍼')
                    if (i.top!=369 and i.top!=397):
                        print('두번째 줄 덱6퍼')
                    if (i.top==397):
                        print('세번째 줄 덱6퍼')
                        
                for i in pyautogui.locateAllOnScreen('luk3.png', confidence=0.90):
                    print('luk3')
                    print(i.top)
                    if (i.top==367):
                        print('첫번째 줄 럭3퍼')
                    if (i.top==382):
                        print('두번째 줄 럭3퍼')
                    if (i.top==396):
                        print('세번째 줄 럭3퍼')
                        
                for i in pyautogui.locateAllOnScreen('luk6.png', confidence=0.95):
                    print('luk6')
                    print(i.top)
                    if (i.top==367):
                        print('첫번째 줄 럭6퍼')
                    if (i.top==383):
                        print('두번째 줄 럭6퍼')
                    if (i.top==397):
                        print('세번째 줄 럭6퍼')
                        
                for i in pyautogui.locateAllOnScreen('int3.png', confidence=0.92):
                    print('int3')
                    print(i.top)
                    if (i.top==369):
                        print('첫번째 줄 인트3퍼')
                    if (i.top==383):
                        print('두번째 줄 인트3퍼')
                    if (i.top==397):
                        print('세번째 줄 인트3퍼')
                        
                for i in pyautogui.locateAllOnScreen('int6.png', confidence=0.97):
                    print('int6')
                    print(i.top)
                    if (i.top==369):
                        print('첫번째 줄 인트6퍼')
                    if (i.top==382):
                        print('두번째 줄 인트6퍼')
                    if (i.top==397):
                        print('세번째 줄 인트6퍼')
