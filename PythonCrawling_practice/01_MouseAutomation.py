import pyautogui
import time


# 1. 화면 크기 출력
print(pyautogui.size())


# 2. 마우스 위치 출력
print(pyautogui.position())
# 2.1. 2초 뒤의 마우스 위치 출력
time.sleep(2)
print(pyautogui.position())


# 3. 마우스 이동
pyautogui.moveTo(41, 442)
# 3.1. 마우스 이동 (세 번째 인자는 이동에 소요되는 시간)
pyautogui.moveTo(442, 30, 3)


# 4. 마우스 클릭
pyautogui.click()
# 4.1. 마우스 우클릭
pyautogui.click(button='right')
# 4.3 마우스 더블클릭
pyautogui.doubleClick()
# 4.3 마우스 3번 클릭__1초마다
pyautogui.click(clicks=3, interval=1)


# 5. 마우스 드래그 (800, 60 --> 60,800)
pyautogui.moveTo(800, 60)
pyautogui.drag(60, 800, 2)


# 6. 마우스 정보 확인창 출력
pyautogui.mouseInfo()