import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(652, 808) # Clicks infernal map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)

    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(15)

    """ Place Ben """
    auto.moveTo(1900, 759)
    direct.press('u')
    time.sleep(1)
    auto.click(1900, 759)
    time.sleep(10)

    """ Place Sniper """
    auto.moveTo(320, 794)
    direct.press('z')
    time.sleep(1)
    auto.click(320, 794)
    auto.click(320, 794)
    time.sleep(10)
    direct.press('/') # Faster firing
    time.sleep(15)
    direct.press('/') # Even faster firing
    time.sleep(120)
    direct.press('/') # Semi automatic rifle
    time.sleep(10)
    direct.press(',') # Full metal jacket
    time.sleep(80)
    direct.press('/') # Full auto rifle
    time.sleep(10)
    direct.press(',') # Large Calibre
    time.sleep(5)

    """ Place Sniper """
    auto.moveTo(333, 666)
    direct.press('z')
    auto.click(333, 666)
    auto.click(333, 666)
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

if __name__ == "__main__":
    playMap()