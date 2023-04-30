import difflib
import re

import pytesseract
from PIL import Image

import const

directory = "data/eachTag"


def read_tag(image, tag_list):
    # match all non-alphanumeric characters except for spaces and -
    # I don't want to match .
    try:
        regex = re.compile('[^a-zA-Z0-9 -]')
        tag_name = pytesseract.image_to_string(image).rstrip("\n")
        tag_name = regex.sub('', tag_name)
        # also check if there is a leading character and a space it must be nonsense so remove it
        if (not tag_name[0].isspace() and tag_name[1] == ' '):
            tag_name = tag_name[2:]
        # or there is a trailing space and then anything but a space it is also nonsense
        if (tag_name[-2] == ' ' and not tag_name[-1].isspace()):
            tag_name = tag_name[:-2]
        tag_name = tag_name.strip()
        tag_name = difflib.get_close_matches(tag_name, const.ALL_TAGS, 1, 0.5)[0]
        if not const.ENABLE_STARTER_TAG:
            if tag_name == "Starter":
                return
        tag_list.append(tag_name)
    except Exception as e:
        print(e)
        print("Error reading tag")

# this function will create the tags from the image by cropping the image and saving it to the specified folder
def createTags():
    if const.SAVE_TO_MEMORY:
        path = const.BUFFER
    else:
        path = const.SCREENSHOT_PATH
    im = Image.open(path)
    width, height = im.size
    tag_location_list = []
    firstTagX = width * 470 / 1600  # 470 on a 1600x900 screen it is at 470, so 470/1600 = 0.29375
    firstTagY = height * 435 / 867  # 435 on a 1600x867 screen it is at 435, so 435/867 = 0.501445
    tagLen = width * 178 / 1600  # 178 on a 1600x900 screen it is at 178, so 178/1600 = 0.11125
    tagHeight = height * 53 / 867  # 53 on a 1600x867 screen it is at 53, so 53/867 = 0.0611
    gapLen = width * 31 / 1600  # 29 on a 1600x900 screen it is at 29, so 29/1600 = 0.018125
    gapHeight = height * 32 / 867  # 29 on a 1600x867 screen it is at 29, so 29/867 = 0.03333333333333333
    for i in range(5):
        start_x = firstTagX + (i % 3) * (gapLen + tagLen)
        start_y = firstTagY + (i % 2) * (gapHeight + tagHeight)
        box = (start_x, start_y, start_x + tagLen, start_y + tagHeight)
        tag_location_list.append(box)
    return tag_location_list

def get_tag_list():
    tagList = []
    tag_location_list = createTags()
    for i in range(len(tag_location_list)):
        if const.SAVE_TO_MEMORY:
            image = Image.open(const.BUFFER).crop(tag_location_list[i])
        else:
            image = Image.open(const.SCREENSHOT_PATH).crop(tag_location_list[i])
        read_tag(image, tagList)
        image.close()
    print(tagList)
    return tagList
