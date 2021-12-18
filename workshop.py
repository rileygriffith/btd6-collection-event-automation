import pyautogui as auto
import pydirectinput as direct
import time

auto.PAUSE = 2

def playMap():
    """ Menu Stuff """
    auto.click(1388, 698) # Clicks workshop map
    auto.click(782, 638) # Easy
    auto.click(746, 804) # Standard
    time.sleep(10)


    """ Place Dart Monkey """
    auto.moveTo(1300, 642)
    direct.press('q')
    time.sleep(1)
    auto.click(1300, 642)
    
    auto.click(1935, 1312) # Start button
    auto.click(1935, 1312) # Fast forward
    time.sleep(8)

    """ Place Ben """
    auto.moveTo(1546, 421)
    direct.press('u')
    time.sleep(1)
    auto.click(1546, 421)
    time.sleep(12)

    """ Place Wizard """
    auto.moveTo(432, 804)
    direct.press('a')
    time.sleep(1)
    auto.click(432, 804)
    auto.click(432, 804)
    time.sleep(5)
    direct.press('.') # Fireball upgrade
    time.sleep(15)
    direct.press('.') # Wall of fire upgrade
    time.sleep(20)

    """ Place spike factory """
    auto.moveTo(1924, 801)
    direct.press('j')
    auto.click(1924, 801)
    auto.click(1924, 801)
    direct.press('/') # Long reach spikes upgrade
    time.sleep(5)
    direct.press('/') # Smart spikes upgrade
    time.sleep(20)
    direct.press(',') # Bigger stacks upgrade
    time.sleep(10)
    direct.press(',') # White hot spikes upgrade
    time.sleep(20)

    """ Place spike factory """
    auto.moveTo(1929, 881)
    direct.press('j')
    auto.click(1929, 881)
    auto.click(1929, 881)
    direct.press('/') # Long reach spikes upgrade
    time.sleep(5)
    direct.press('/') # Smart spikes upgrade
    time.sleep(20)
    direct.press(',') # Bigger stacks upgrade
    time.sleep(10)
    direct.press(',') # White hot spikes upgrade
    for i in range(115): # AFK Till win
        auto.click(1500, 952)