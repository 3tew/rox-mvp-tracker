# Initialize Global Variables
IS_DEVELOPMENT = True
IS_RUNNING = True
VERSION = '1.0'
TITLE = 'RO:X Next Generation - MVP Tracker version ' + VERSION
FULL_TITLE = ''
PID = ''
VERSION = '1.0'

CURRENT_TIME = 0
PREV_TIME = 0
SCREENSHOT = None

EMULATOR = 1  # BlueStacks App Player
EMULATOR_TEXT = 'BlueStacks App Player'
EMULATOR_X = 0
EMULATOR_Y = 0
EMULATOR_WIDTH = 0
EMULATOR_HEIGHT = 0

FRAME_EMULATOR = None
FRAME_EMULATOR_RGB = None
FRAME_EMULATOR_HSV = None

ZAPIER_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/11095029/bt0yqsf/silent/"

NOTICE_BOUNDING_BOX = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
NOTICE_TIME = 0
FRAME_NOTICE_TEXT = None

BOSS_STATUS_BOUNDING_BOX_0 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_1 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_2 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_3 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_4 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}

FRAME_BOSS_STATUS_BOX_1 = None
FRAME_BOSS_STATUS_BOX_2 = None
FRAME_BOSS_STATUS_BOX_3 = None
FRAME_BOSS_STATUS_BOX_4 = None

MOUSE_DRAG_CENTER_X_1 = 0
MOUSE_DRAG_CENTER_Y_1 = 0
MOUSE_DRAG_CENTER_X_2 = 0
MOUSE_DRAG_CENTER_Y_2 = 0

MVP_BOUNDING_BOX = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
MVP_BOUNDING_BOX_CENTER_X = 0
MVP_BOUNDING_BOX_CENTER_Y = 0

MINI_BOUNDING_BOX = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
MINI_BOUNDING_BOX_CENTER_X = 0
MINI_BOUNDING_BOX_CENTER_Y = 0

BOSS_NAMES = [
    'Phreeoni',
    'Mistress',
    'Kraken',
    'Eddga',
    'Maya',
    'Pharaoh',
    'Orc Hero',
    'Hero',
    'Orc Lord',
    'Lord',
    'Eclipse',
    'Mastering',
    'Ghosting',
    'Toad',
    'Dragon Fly',
    'Dragon',
    'Fly',
    'King Dramoh',
    'King',
    'Dramoh',
    'Angeling',
    'Deviling',
]

MVP_SPAWNED_TIME = {
    'phreeoni': 0,
    'mistress': 0,
    'kraken': 0,
    'eddga': 0,
    'orchero': 0,
    'maya': 0,
    'pharaoh': 0,
    'orclord': 0,
}

MINI_SPAWNED_TIME = {
    'eclipse': 0,
    'dragonfly': 0,
    'mastering': 0,
    'ghosting': 0,
    'kingdramoh': 0,
    'toad': 0,
    'angeling': 0,
    'deviling': 0,
}
