import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(1622, 535) # Clicks muddy puddles map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)

    """ Place Dart Monkey """
    auto.moveTo(1436, 768)
    direct.press('q')
    time.sleep(1)
    auto.click(1436, 768)

    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(12)

    """ Place Ben """
    auto.moveTo(1035, 269)
    direct.press('u')
    time.sleep(1)
    auto.click(1035, 269)
    time.sleep(10)

    """ Place Sniper """
    auto.moveTo(816, 1086)
    direct.press('z')
    time.sleep(1)
    auto.click(816, 1086)
    auto.click(816, 1086)
    time.sleep(10)
    direct.press('/') # Faster firing
    time.sleep(10)
    direct.press('/') # Even faster firing
    time.sleep(88)
    direct.press('/') # Semi automatic rifle
    time.sleep(10)
    direct.press(',') # Full metal jacket
    time.sleep(60),
    direct.press('/') # Full auto rifle
    time.sleep(10)
    direct.press(',') # Large Calibre
    time.sleep(5)

    """ Place Sniper """
    auto.moveTo(708, 827)
    direct.press('z')
    auto.click(708, 827)
    auto.click(708, 827)
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