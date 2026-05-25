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


def create_tag_list(image) -> list[tuple[int, int, int, int]]:
    width, height = image.size
    tag_location_list = []
    firstTagX = int(width * 0.02)
    firstTagY = int(height * 0.05)
    tagLen = int(width * 0.29)
    tagHeight = int(height * 0.36)
    gapLen = int(width * 0.04)
    gapHeight = int(height * 0.18)
    for i in range(5):
        start_x = firstTagX + (i % 3) * (gapLen + tagLen)
        start_y = firstTagY + (i % 2) * (gapHeight + tagHeight)
        box = (start_x, start_y, start_x + tagLen, start_y + tagHeight)
        tag_location_list.append(box)
    return tag_location_list


def get_tag_list():
    image = Image.open(const.BUFFER if const.SAVE_TO_MEMORY else const.SCREENSHOT_PATH)
    tag_location_list = create_tag_list(image)
    tag_list = []
    for i in range(len(tag_location_list)):
        img_crop = image.crop(tag_location_list[i])
        read_tag(img_crop, tag_list)
        img_crop.close()
    image.close()
    print(tag_list)
    return tag_list

if __name__ == "__main__":
    get_tag_list()