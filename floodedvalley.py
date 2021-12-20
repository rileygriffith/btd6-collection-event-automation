import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """Navigating the menu"""
    auto.click(1622, 535) # Clicks the map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)
    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(10)

    """ Place Ben """
    direct.press('u')
    time.sleep(1)
    auto.click(879, 606)
    time.sleep(6)

    """ Place Buccaneer """
    auto.moveTo(1350, 952)
    direct.press('c')
    time.sleep(1)
    auto.click(1350, 952)
    auto.click(1350, 952)
    time.sleep(5)
    
    """ Upgrades """
    direct.press(',') # Faster shooting
    time.sleep(12)
    direct.press('.') # Grape shot
    time.sleep(25)
    direct.press(',') # Double shot
    time.sleep(35)
    direct.press('.') # Hot shots
    time.sleep(70)
    direct.press(',') # Destroyer
    for i in range(110): # AFK Till win
        auto.click(1500, 952)

if __name__ == "__main__":
    playMap()