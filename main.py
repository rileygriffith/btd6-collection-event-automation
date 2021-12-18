import pyautogui as auto
import pydirectinput as direct
import time
from PIL import ImageGrab

import floodedvalley
import workshop
import ouch
import bloodypuddles
import sanctuary
import quad
import darkcastle
import infernal
import muddypuddles
import ravine

auto.PAUSE = 2

def main():
    # DEBUG
    # time.sleep(2)
    # print(ImageGrab.grab().getpixel(auto.position()), auto.position())
    # return None
    while True:
        """ Navigate main menu"""
        time.sleep(2)
        auto.click(977, 1235) # Play
        auto.click(1553, 1271) # Expert

        """ Detect which map is bonus """
        if not ImageGrab.grab().getpixel((1771, 799))[1] and not ImageGrab.grab().getpixel((1771, 799))[2]:
            workshop.playMap()
        elif not ImageGrab.grab().getpixel((1321, 799))[1] and not ImageGrab.grab().getpixel((1321, 799))[2]:
            bloodypuddles.playMap()
        elif not ImageGrab.grab().getpixel((863, 465))[1] and not ImageGrab.grab().getpixel((863, 465))[2]:
            sanctuary.playMap()
        elif not ImageGrab.grab().getpixel((1772, 465))[1] and not ImageGrab.grab().getpixel((1772, 465))[2]:
            floodedvalley.playMap()
        elif not ImageGrab.grab().getpixel((861, 802))[1] and not ImageGrab.grab().getpixel((861, 802))[2]:
            infernal.playMap()
        elif not ImageGrab.grab().getpixel((1314, 465))[1] and not ImageGrab.grab().getpixel((1314, 465))[2]:
            ravine.playMap()
        else: # We need to go to the next page
            auto.click(1856, 659)
            if not ImageGrab.grab().getpixel((861, 802))[1] and not ImageGrab.grab().getpixel((861, 802))[2]:
                ouch.playMap()
            elif not ImageGrab.grab().getpixel((863, 465))[1] and not ImageGrab.grab().getpixel((863, 465))[2]:
                quad.playMap()
            elif not ImageGrab.grab().getpixel((1314, 465))[1] and not ImageGrab.grab().getpixel((1314, 465))[2]:
                darkcastle.playMap()
            elif not ImageGrab.grab().getpixel((1772, 465))[1] and not ImageGrab.grab().getpixel((1772, 465))[2]:
                muddypuddles.playMap()

        """ Return back to menu """
        auto.click(1122, 1178) # Next
        auto.click(870, 1097) # Home
        time.sleep(10)

if __name__ == "__main__":
    main()