import pyautogui as pg
from random import randint
import time
import os

# mouse move

# for i in range(5):
    # height = randint(0,1080)
    # weight = randint(0,1920)
    # pg.click(weight, height, duration=0.2)
    # pg.write("Hello world", interval=0.25)
    # pg.hotkey('command', 'v')


# pg.alert(text='Hello', title="HI", button="OK")

os.system("open -a Notes" )
time.sleep(2)
pg.click(x=870, y=510)
pg.write("Hello world", interval=0.1)

    
    









