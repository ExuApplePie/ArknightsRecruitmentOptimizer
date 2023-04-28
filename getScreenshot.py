from time import sleep

import pygetwindow
from PIL import Image
from PIL import ImageGrab

import const


def get_screenshot():
    try:
        win = pygetwindow.getWindowsWithTitle(const.emulator_name)[0]
    except:  # if the emulator is not open terminate the program
        print("Emulator not open")
        return -1
    win.minimize()
    win.restore()
    win.size = const.emulator_size  # equivalent to win.size = (1600, 900)
    sleep(0.1)
    left, top, right, bottom = win.left, win.top, win.right, win.bottom
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    img.save(const.screenshot_path)
    img = Image.open(const.screenshot_path)
    width, height = img.size
    img = img.crop((0, 33, width, height))  # 33 because bluestacks has a thing on top that is 33 pixels tall
    img.save(const.screenshot_path)
    img.close()
    # minimize the window so it doesn't get in the way
    win.minimize()
