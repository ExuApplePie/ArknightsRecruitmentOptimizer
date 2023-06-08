from io import BytesIO
from os import path
WEBSITE = "https://gamepress.gg/arknights/tools/arknights-recruitment-tag-filter" # "https://aceship.github.io/AN-EN-Tags/akhr.html" - not maintained enough
EMULATOR_NAME = 'arknights_emulator'  # set to your emulator name
EMULATOR_SIZE = (1600, 900)  # set to your emulator size - shouldn't actually matter as long as your monitor >= this size
IS_BLUESTACKS = True  # set to False if using Nox or any emulator that doesn't have something on top
BLUESTACKS_TOP = 33 if IS_BLUESTACKS else 0  # or set to whatever you need
IMAGE_SIZE = (1600, EMULATOR_SIZE[1] - BLUESTACKS_TOP)  # probably don't change this - unused if SAVE_TO_MEMORY is True
# full list is: Starter, Senior Operator, Top Operator, Melee, Ranged, Guard, Medic, Vanguard, Caster, Sniper, Defender, Supporter, Specialist, Healing, Support, DPS, AoE, Slow, Survival, Defense, Debuff, Shift, Crowd Control, Nuker, Summon, Fast-Redeploy, Robot, DP-Recovery
ALL_TAGS = ['Starter', 'Senior-Operator', 'Top-Operator', 'Melee', 'Ranged', 'Guard', 'Medic', 'Vanguard', 'Caster',
            'Sniper', 'Defender', 'Supporter', 'Specialist', 'Healing', 'Support', 'DPS', 'AoE', 'Slow', 'Survival',
            'Defense', 'Debuff', 'Shift', 'Crowd-Control', 'Nuker', 'Summon', 'Fast-Redeploy', 'Robot', 'DP-Recovery']
SCREENSHOT_PATH = path.normpath("data/tagScreenshot.jpg")  # probably don't change this
ENABLE_STARTER_TAG = False  # set to True if you want to enable the starter tag
# set keys you want to use to control the program
INPUT_TAG_KEY = '`'
SHOW_EMULATOR_KEY = '1'
END_PROGRAM_KEY = '.'
SAVE_TO_MEMORY = True  # set to False if you want to save to disk instead
BUFFER = BytesIO()
