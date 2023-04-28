from time import sleep

import pygetwindow
from PIL import ImageGrab

import const


def get_screenshot():
    try:
        win = pygetwindow.getWindowsWithTitle(const.EMULATOR_NAME)[0]
    except:  # if the emulator is not open terminate the program
        print("Emulator not open")
        return -1
    win.minimize()
    win.restore()
    win.size = const.EMULATOR_SIZE  # equivalent to win.size = (1600, 900)
    sleep(0.1)
    left, top, right, bottom = win.left, win.top, win.right, win.bottom
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    width, height = img.size
    img.crop((0, 33, width, height))
    if const.SAVE_TO_MEMORY:
        # clear buffer - more like jump to the beginning of the buffer
        const.BUFFER.seek(0)
        img.save(const.BUFFER, 'JPEG')
    else:
        img.save(const.SCREENSHOT_PATH)
    # minimize the window so it doesn't get in the way
    win.minimize()
