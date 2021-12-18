import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(652, 808) # Clicks ouch map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)

    """ Place Dart Monkey """
    auto.moveTo(808, 435)
    direct.press('q')
    time.sleep(1)
    auto.click(808, 435)

    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(12)

    """ Place Ben """
    auto.moveTo(1553, 390)
    direct.press('u')
    time.sleep(1)
    auto.click(1553, 390)
    time.sleep(10)

    """ Place Buccaneer """
    auto.moveTo(1135, 711)
    direct.press('c')
    auto.click(1135, 711)
    auto.click(1135, 711)
    time.sleep(10)
    direct.press(',') # Faster shooting
    time.sleep(12)
    direct.press('.') # Grape shot
    time.sleep(25)
    direct.press(',') # Double shot
    time.sleep(30)
    direct.press('.') # Hot shots
    time.sleep(70)
    direct.press(',') # Destroyer
    for i in range(115): # AFK Till win
        auto.click(1500, 952)

time.sleep(2)
print(auto.position())