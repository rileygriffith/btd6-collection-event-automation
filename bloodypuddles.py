import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(1109, 785) # Clicks bloody puddles map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)

    """ Place Dart Monkey """
    auto.moveTo(585, 306)
    direct.press('q')
    time.sleep(1)
    auto.click(585, 306)

    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(12)

    """ Place Ben """
    auto.moveTo(1128, 580)
    direct.press('u')
    time.sleep(1)
    auto.click(1128, 580)
    time.sleep(5)

    """ Place Sub """
    auto.moveTo(1505, 323)
    direct.press('x')
    time.sleep(1)
    auto.click(1505, 323)
    auto.click(1505, 323)
    time.sleep(10)
    direct.press(',') # Longer range
    time.sleep(10)
    direct.press(',') # Advanced Intel
    time.sleep(10)
    direct.press('/') # Twin guns
    time.sleep(25)
    direct.press('/') # Airburst darts
    time.sleep(25)
    direct.press('/') # Triple guns
    time.sleep(10)

    """ Place Sniper """
    auto.moveTo(1129, 257)
    direct.press('z')
    time.sleep(1)
    auto.click(1129, 257)
    auto.click(1129, 257)
    direct.press('tab')
    direct.press('tab')
    direct.press('tab') # Change to strong targeting
    time.sleep(10)
    direct.press(',') # Full metal jacket
    time.sleep(10)
    direct.press('/') # Faster firing
    time.sleep(10)
    direct.press('/') # Even faster firing
    time.sleep(10)

    """ Place Buccaneer """
    auto.moveTo(891, 775)
    direct.press('c')
    time.sleep(1)
    auto.click(891, 775)
    auto.click(891, 775)
    time.sleep(10)
    direct.press('.') # Grape shot
    time.sleep(10)
    direct.press(',') # Faster shooting
    time.sleep(10)
    direct.press(',') # Double shot
    for i in range(90): # AFK Till win
        auto.click(1500, 952)

if __name__ == "__main__":
    playMap()