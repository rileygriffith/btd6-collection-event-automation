import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(1112, 476) # Clicks dark castle map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)

    """ Place dart monkey """
    auto.moveTo(427, 639)
    direct.press('q')
    time.sleep(1)
    auto.click(427, 639)

    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(14)

    """ Place Ben """
    auto.moveTo(1627, 506)
    direct.press('u')
    time.sleep(1)
    auto.click(1627, 506)
    time.sleep(5)

    """ Place Sniper """
    auto.moveTo(548, 979)
    direct.press('z')
    time.sleep(1)
    auto.click(548, 979)
    auto.click(548, 979)
    time.sleep(10)
    direct.press('/') # Faster firing
    time.sleep(12)
    direct.press('/') # Even faster firing
    time.sleep(100)
    direct.press('/') # Semi automatic rifle
    time.sleep(10)
    direct.press(',') # Full metal jacket
    time.sleep(70)
    direct.press('/') # Full auto rifle
    time.sleep(10)
    direct.press(',') # Large Calibre
    time.sleep(5)

    """ Place Sniper """
    auto.moveTo(1020, 985)
    direct.press('z')
    auto.click(1020, 985)
    auto.click(1020, 985)
    time.sleep(10)
    direct.press('.') # Night vision goggles
    time.sleep(10)
    direct.press('.') # Shrapnel shot
    time.sleep(10)
    direct.press('/') # Faster firing
    time.sleep(10)
    direct.press('/') # Even faster firing
    time.sleep(10)
    direct.press('/') # Semi automatic rifle
    time.sleep(45)
    direct.press('/') # Full auto rifle

    for i in range(30): # AFK Till win
        auto.click(1500, 952)