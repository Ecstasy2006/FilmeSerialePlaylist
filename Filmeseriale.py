from time import sleep
from pyautogui import press, click, locateCenterOnScreen, move
import sys

for i in range(1):
    #time of the movie in seconds
    sleep(63*60)
    press('esc')
    sleep(1)
    #image of the next video button
    click(locateCenterOnScreen('next.png'))
    move(0, 200)
    sleep(3)
    click()
    #w8 for commercials
    sleep(15)
    click()
    sleep(1)
    #fullscreen
    press('f')
    sleep(1)
    #play the movie
    press('space')