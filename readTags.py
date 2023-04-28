import difflib
import os
from PIL import Image
import pytesseract
import re
import const

directory = "data/eachTag"


def read_tag(file_path, tag_list):
    # match all non-alphanumeric characters except for spaces and -
    # I don't want to match .
    try:
        regex = re.compile('[^a-zA-Z0-9 -]')
        tag_name = pytesseract.image_to_string(Image.open(file_path)).rstrip("\n")
        tag_name = regex.sub('', tag_name)
        # also check if there is a leading character and a space it must be nonsense so remove it
        if (not tag_name[0].isspace() and tag_name[1] == ' '):
            tag_name = tag_name[2:]
        # or there is a trailing space and then anything but a space it is also nonsense
        if (tag_name[-2] == ' ' and not tag_name[-1].isspace()):
            tag_name = tag_name[:-2]
        tag_name = tag_name.strip()
        tag_name = difflib.get_close_matches(tag_name, const.all_tags, 1, 0.5)[0]
        tag_list.append(tag_name)
    except Exception as e:
        print(e)
        print("Error reading tag")

def get_tag_list():
    tagList = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            read_tag(f, tagList)
    print(tagList)
    return tagList




