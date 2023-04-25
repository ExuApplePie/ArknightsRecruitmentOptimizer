import os
from PIL import Image
import pytesseract
import re

directory = "data/eachTag"


def readTag(filePath, tagList):
    # match all non-alphanumeric characters except for spaces and -
    # I don't want to match .
    regex = re.compile('[^a-zA-Z0-9 -]')
    str = pytesseract.image_to_string(Image.open(filePath)).rstrip("\n")
    str = regex.sub('', str)
    tagList.append(str)

def getTagList():
    tagList = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            readTag(f, tagList)
    print(tagList)
    return tagList




