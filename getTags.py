import time

from PIL import Image
from tkinter.filedialog import askopenfilename

import pytesseract

def is_locked(filepath):
    locked = None
    file_object = None
    if os.path.exists(filepath):
        try:
            buffer_size = 8
            # Opening file in append mode and read the first 8 characters.
            file_object = open(filepath, 'a', buffer_size)
            if file_object:
                locked = False
        except IOError as message:
            locked = True
        finally:
            if file_object:
                file_object.close()
    return locked

def wait_for_file(filepath):
    wait_time = 1
    while is_locked(filepath):
        time.sleep(wait_time)

try:
    # pathToFile = r'C:\Users\niclo\Pictures\p.jpg'
    # wait_for_file(pathToFile)
    pathToFile = askopenfilename()
    image = Image.open(pathToFile)
    print(pytesseract.image_to_string(image))
    print("ran succesfully")
except:
    print("FileNotFound")

