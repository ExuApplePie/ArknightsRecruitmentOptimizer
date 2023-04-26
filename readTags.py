import os
from PIL import Image
import pytesseract
import re

directory = "data/eachTag"


def readTag(filePath, tagList):
    # match all non-alphanumeric characters except for spaces and -
    # I don't want to match .
    try:
        regex = re.compile('[^a-zA-Z0-9 -]')
        str = pytesseract.image_to_string(Image.open(filePath)).rstrip("\n")
        str = regex.sub('', str)
        # also check if there is a leading character and a space it must be nonsense so remove it
        if (str[0].isalpha() and str[1] == ' '):
            str = str[2:]
        # or there is a trailing space and then a character it is also nonsense
        if (str[-2] == ' ' and str[-1].isalpha()):
            str = str[:-2]
        str = str.strip()
        tagList.append(str)
    except Exception as e:
        print(e)
        print("Error reading tag")

def getTagList():
    tagList = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            readTag(f, tagList)
    print(tagList)
    return tagList




