from PIL import Image

import const


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
