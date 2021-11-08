import pyautogui
import pyperclip


# 1. write() 함수
pyautogui.write('My name is Choi Jiwon')
# 1.1 간격을 두고 타이핑 (0.1초마다)
pyautogui.write('My name is Choi Jiwon', interval=0.1)
# 1.2 한글을 타이핑하는 경우 (pyautogui는 한글에 대한 적용이 안되어있음.)
pyperclip.copy('국민대학교 소프트웨어학부') # 클립보드에 텍스트 복사
pyautogui.hotkey('ctrl', 'v') # 복사된 텍스트 붙여넣기 (hotkey 사용)


# 2. press(), keyDown(), keyUp() 함수
# 2.1. press() 함수
pyautogui.press('shift') # shift 키를 누름.
pyautogui.press('ctrl') # ctrl 키를 누름.
# 2.2. keyDown() 함수
pyautogui.keyDown('ctrl') # ctrl 키를 누른 상태로 유지함.
pyautogui.press('c') # c 키를 누름.
pyautogui.keyUp('ctrl') # ctrl 키를 뗌.
# 2.3. 키를 여러 번 입력하는 경우
pyautogui.press(['left', 'left', 'left']) # 왼쪽 방향키를 세번 입력함.
pyautogui.press('left', presses=3) # 왼쪽 방향키를 세번 입력함
pyautogui.press('enter', presses=3, interval=3) # enter 키를 3초에 한번씩 세번 입력함.


# 3. hotkey() 함수
# 여러 키를 동시에 입력해야 할 경우, keyDown과 keyUp 을 사용하게 되면 코드가 복잡해짐.
# --> hoykey 를 이용하여 해당 부분을 보완할 수 있음.
pyautogui.hotkey('ctrl', 'c') # ctrl + c 키를 입력함. (복사)