from pyautogui import *
from time import sleep
from random import Random
random = Random()
a = ['a', 's', 'd', 'w', 'space']
pause = 30
FAILSAFE = False
while True:
    for i in range(random.randint(0, 3)):
        key = a[random.randint(0, len(a))-1]
        keyDown(key)
        sleep(random.uniform(0, 1.5))
        keyUp(key)
    sleep(pause + random.uniform(0, pause/2))
