import os

from PIL import Image

import const

def crop_image(input_image, output_image, start_x, start_y, width, height):
    """Pass input name image, output name image, x coordinate to start croping, y coordinate to start croping, width to crop, height to crop """
    input_img = Image.open(input_image)
    box = (start_x, start_y, start_x + width, start_y + height)
    output_img = input_img.copy().crop(box)
    # create a new file if not exist in png format
    directory = os.path.normpath("data/eachTag")
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        output_img.save(output_image + ".png")
    except (KeyError, IOError) as e:
        print(e)
    # close image
    output_img.close()
    input_img.close()


# this function will create the tags from the image by cropping the image and saving it to the specified folder
def createTags():
    path = const.screenshot_path
    im = Image.open(path)
    width, height = im.size
    im.close()
    firstTagX = width * 470 / 1600  # 470 on a 1600x900 screen it is at 470, so 470/1600 = 0.29375
    firstTagY = height * 435 / 867  # 435 on a 1600x867 screen it is at 435, so 435/867 = 0.501445
    tagLen = width * 178 / 1600  # 178 on a 1600x900 screen it is at 178, so 178/1600 = 0.11125
    tagHeight = height * 53 / 867  # 53 on a 1600x867 screen it is at 53, so 53/867 = 0.0611
    gapLen = width * 31 / 1600  # 29 on a 1600x900 screen it is at 29, so 29/1600 = 0.018125
    gapHeight = height * 32 / 867  # 29 on a 1600x867 screen it is at 29, so 29/867 = 0.03333333333333333
    for i in range(5):
        # f makes it format the string
        crop_image(path, os.path.normpath(f"data/eachTag/tag{i}"),
                   firstTagX + (i % 3) * (gapLen + tagLen),
                   firstTagY + (i % 2) * (gapHeight + tagHeight), tagLen, tagHeight)
