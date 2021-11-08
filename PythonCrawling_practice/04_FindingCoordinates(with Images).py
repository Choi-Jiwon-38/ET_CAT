import pyautogui as pg

# 1 Locate 함수
buttonCalLocation = pg.locateOnScreen('calButton.png') # 이미지 calButton.png 가 있는 위치를 가져옴 
print(buttonCalLocation)

# 2. center 함수
point = pg.center('calButton.png') # Box 객체의 중앙 좌표를 리턴합니다. 
print(point)