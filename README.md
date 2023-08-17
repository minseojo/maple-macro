# 만든이유
메이플스토리 게임을 하는데, 내가 원하는 옵션을 뽑기 위해서는 `수상한 큐브`라는 아이템을 돌려서 내가 원하는 옵션이 나올 때 까지 반복해서 돌려야 했다. <br>
이 불편함을 매크로로 해결하기 위해 만들었다.

---
# 작동원리
1. 메이플스토리 화면을 모니터 상단 왼쪽에 고정시킨다. (pyautogui)
2. 메이플 인벤토리 창을 화면에 고정 시킨다. (pyautogui)
3. 큐브 각각의 옵션 3개를 이미지로 가져온다. (opencv)
4. 이미지에는 STR 3%, DEX 6%, 공격력 6% 등등의 옵션이 있는데, 이 옵션 이미지를 문자열로 바꾼다. (OCR-Tesseract)
   ex) STR 3% (IMAGE) -> STR 3% (STRING)
5. 문자열을 비교해 내가 원하는 스탯이 맞는지 비교해서 맞다면 현재 아이템 큐브 돌리는것을 멈추고, 다음 아이템으로 넘어간다. (최대 128개 아이템)
---
# 프로그램 화면
![image](https://github.com/minseojo/maple-macro/assets/64322765/a2148885-52c5-4a7c-9f11-7c8d95063967)


##
처음에는 굳이 이미지를 바꿔야해? 그냥 STR 6% 이미지 저장해놓고, 이미지끼리 비교하면 안되나? <br>
이런식으로 구현했었는데, 내가 원하는대로 작동이 안되서 OCR을 이용했다.
