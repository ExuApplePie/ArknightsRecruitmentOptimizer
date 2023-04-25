import os
from PIL import Image
import pytesseract

directory = "data/eachTag"
tagList = []

def readTag(filePath):
    tagList.append(pytesseract.image_to_string(Image.open(filePath)).rstrip("\n"))

def getTags():
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            readTag(f)
    print(tagList)
    return tagList




