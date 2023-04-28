from io import BytesIO
from os import path

EMULATOR_NAME = 'arknights_emulator'  # set to your emulator name
EMULATOR_SIZE = (1600, 900)  # set to your emulator size
IMAGE_SIZE = (1600, 867)  # probably don't change this
# full list is: Starter, Senior Operator, Top Operator, Melee, Ranged, Guard, Medic, Vanguard, Caster, Sniper, Defender, Supporter, Specialist, Healing, Support, DPS, AoE, Slow, Survival, Defense, Debuff, Shift, Crowd Control, Nuker, Summon, Fast-Redeploy, Robot, DP-Recovery
ALL_TAGS = ['Starter', 'Senior Operator', 'Top Operator', 'Melee', 'Ranged', 'Guard', 'Medic', 'Vanguard', 'Caster',
            'Sniper', 'Defender', 'Supporter', 'Specialist', 'Healing', 'Support', 'DPS', 'AoE', 'Slow', 'Survival',
            'Defense', 'Debuff', 'Shift', 'Crowd Control', 'Nuker', 'Summon', 'Fast-Redeploy', 'Robot', 'DP-Recovery']
SCREENSHOT_PATH = path.normpath("data/tagScreenshot.jpg")  # probably don't change this
ENABLE_STARTER_TAG = False  # set to True if you want to enable the starter tag
# set keys you want to use to control the program
INPUT_TAG_KEY = '`'
SHOW_EMULATOR_KEY = '1'
END_PROGRAM_KEY = '.'
IS_BLUESTACKS = True  # set to False if using Nox or any emulator that doesn't have something on top
BLUESTACKS_TOP = 33 if IS_BLUESTACKS else 0  # or set to whatever you need
SAVE_TO_MEMORY = True  # set to False if you want to save to disk instead
BUFFER = BytesIO()
