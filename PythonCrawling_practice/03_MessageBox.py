from collections import defaultdict
from tkinter import Button
import pyautogui as pg # alias

# 1. alert() 함수
msg1 = pg.alert(text = '내용이 써지는 곳입니다', title = '제목이 써지는 곳입니다', button = 'OK')
print(msg1)

# 2. confirm() 함수
msg2 = pg.confirm(text = '내용이 써지는 곳입니다', title = '제목이 써지는 곳입니다', buttons = ['OK', 'Cancel'])
print(msg2)

# 3. prompt() 함수
msg3 = pg.prompt(text = '내용이 써지는 곳입니다', title = '제목이 써지는 곳입니다', default = '입력해주세요')
print(msg3)

# 4. password() 함수
msg4 = pg.password(text = '내용이 써지는 곳입니다', title = '제목이 써지는 곳입니다', default = '입력해주세요', mask = '*')
print(msg4)