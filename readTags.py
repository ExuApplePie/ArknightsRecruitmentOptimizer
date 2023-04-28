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


def get_tag_list(tag_location_list):
    tagList = []
    for i in range(len(tag_location_list)):
        if const.SAVE_TO_MEMORY:
            image = Image.open(const.BUFFER).crop(tag_location_list[i])
        else:
            image = Image.open(const.SCREENSHOT_PATH).crop(tag_location_list[i])
        read_tag(image, tagList)
        image.close()
    print(tagList)
    return tagList
