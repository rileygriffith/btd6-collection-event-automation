import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(670, 476) # Clicks quad map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)

    """ Place dart monkey """
    auto.moveTo(693, 702)
    direct.press('q')
    time.sleep(1)
    auto.click(693, 702)

    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(12)

    """ Place Ben """
    auto.moveTo(591, 1041)
    direct.press('u')
    time.sleep(1)
    auto.click(591, 1041)
    time.sleep(5)

    """ Place Sniper """
    auto.moveTo(868, 688)
    direct.press('z')
    time.sleep(1)
    auto.click(868, 688)
    auto.click(868, 688)
    time.sleep(10)
    direct.press('/') # Faster firing
    time.sleep(12)
    direct.press('/') # Even faster firing
    time.sleep(110)
    direct.press('/') # Semi automatic rifle
    time.sleep(10)
    direct.press(',') # Full metal jacket
    time.sleep(80)
    direct.press('/') # Full auto rifle
    time.sleep(10)
    direct.press(',') # Large Calibre
    time.sleep(5)

    """ Place Sniper """
    auto.moveTo(1463, 714)
    direct.press('z')
    auto.click(1463, 714)
    auto.click(1463, 714)
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