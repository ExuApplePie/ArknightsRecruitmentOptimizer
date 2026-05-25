import sys
from time import sleep
import pygetwindow as gw
from PIL import ImageGrab

import const


def get_screenshot():
    try:
        win = gw.getWindowsWithTitle(const.EMULATOR_NAME)[0]
        # win.minimize()
        # win.restore()
        # win.size = const.EMULATOR_SIZE  # equivalent to win.size = (1600, 900)
        # sleep(0.1)
        # left, top, right, bottom = win.left, win.top, win.right, win.bottom
        img = ImageGrab.grab(window=win._hWnd)
        width, height = img.size
        img = img.crop((int(width * 0.3046), int(height * 0.5159), int(width * 0.6614), int(height * 0.6851)))
        if const.SAVE_TO_MEMORY:
            # clear buffer - more like jump to the beginning of the buffer
            const.BUFFER.seek(0)
            img.save(const.BUFFER, 'JPEG')
        else:
            img.save(const.SCREENSHOT_PATH)
        img.close()
        # minimize the window so it doesn't get in the way
        # win.minimize()
    except:  # if the emulator is not open terminate the program
        print("Emulator not open")
        sys.exit()

    
if __name__ == "__main__":
    get_screenshot()