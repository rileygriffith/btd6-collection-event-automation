import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(670, 476) # Clicks sanctuary map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)

    """ Place dart monkey """
    auto.moveTo(1043, 411)
    direct.press('q')
    time.sleep(1)
    auto.click(1043, 411)

    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(12)

    """ Place Ben """
    auto.moveTo(1741, 1129)
    direct.press('u')
    time.sleep(1)
    auto.click(1741, 1129)
    time.sleep(5)

    """ Place Sniper """ 
    auto.moveTo(972, 293)
    direct.press('z')
    time.sleep(1)
    auto.click(978, 261)
    auto.click(978, 261)
    time.sleep(10)
    direct.press('/') # Faster firing
    time.sleep(12)
    direct.press('/') # Even faster firing
    time.sleep(105)
    direct.press('/') # Semi automatic rifle
    time.sleep(5)
    direct.press(',') # Full metal jacket
    time.sleep(60)
    direct.press('/') # Full auto rifle
    time.sleep(10)
    direct.press(',') # Large Calibre
    for i in range(80): # AFK Till win
        auto.click(1500, 952)

if __name__ == "__main__":
    playMap()