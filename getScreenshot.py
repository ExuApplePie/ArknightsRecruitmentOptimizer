import pygetwindow
from PIL import ImageGrab
from PIL import Image
import os
from time import sleep

def getScreenshots():
    try:
        win = pygetwindow.getWindowsWithTitle('arknights_emulator')[0]
    except: # if the emulator is not open terminate the program
        print("Emulator not open")
        return -1
    # if window size isn't 1600x900, resize it
    if win.size != (1600, 900):
        win.size = (1600, 900)
    win.minimize()
    win.restore()
    sleep(0.1)
    left, top, right, bottom = win.left, win.top, win.right, win.bottom
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    img.save(os.path.normpath("data/tagScreenshot.jpg"))
    img = Image.open(os.path.normpath("data/tagScreenshot.jpg"))
    width, height = img.size
    img = img.crop((0, 33, width, height))
    img.save(os.path.normpath("data/tagScreenshot.jpg"))
    # minimize the window so it doesn't get in the way
    win.minimize()