from PIL import Image
import os

import pytesseract

# image size is 1600x900
# tag size is: 470x450 x 650x510
# roughly 30pi apart from each other both wide and tall
# roughly 0.29375 % of the image horizontally
# roughly 0.5
# tags are %0.01875 apart horizontally
# tags are  %0.03333333333333333 apart vertically
# 0.1125% long
# 0.06666667% tall
#
# ******** TEST CODE ********
# print("\n###########\n")
# print(pytesseract.image_to_string(Image.open("data/crop data/healing tag.png")))
# print(30/1600)
# print(30/900)
# print("\n###########\n")

path = os.path.normpath("data/testdata1.png")
im = Image.open(path)
width, height = im.size
firstTagX = 470
firstTagY = 450
tagLen = 650-470
tagHeight = 510-450

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

# this function will create the tags from the image by cropping the image and saving it to the specified folder
def createTags():
    for i in range(5):
        # f makes it format the string
        crop_image(path, os.path.normpath(f"data/eachTag/tag{i}"),
                   firstTagX + (i % 3) * (30 + tagLen),
                   firstTagY + (i % 2) * (30 + tagHeight), tagLen, tagHeight)





