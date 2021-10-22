# -*- coding: utf-8 -*-
# Initialize Global Variables
DEVELOPER_WEBHOOK = 'https://discord.com/api/webhooks/898584759855382629/bgh3uQKNhyOJYHl2Qv7dWaw8i3NYoxmVgiYyRek-bbGBTjPE7s4gGTH0AIquEVwGYgl5'  # Comtech
IS_DEVELOPMENT = False
IS_RUNNING = True
IS_HOLD = False
IS_DISCONNECTED = False
IS_CRASHED = False
VERSION = '1.7-superfast'
TITLE = 'RO:X Next Generation - MVP Tracker version ' + VERSION
FULL_TITLE = ''
PID = ''

CURRENT_TIME = 0
PREV_TIME = 0
SCREENSHOT = None

EMULATOR_NAMES = ['LDPlayer', 'BlueStacks App Player']
EMULATOR_SELECTED = 'LDPlayer'  # Default
EMULATOR_X = 0
EMULATOR_Y = 0
EMULATOR_WIDTH = 0
EMULATOR_HEIGHT = 0

FRAME_EMULATOR = None
FRAME_EMULATOR_RGB = None

DISCORD_WEBHOOK_URLS = []

NOTICE_BOUNDING_BOX = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
NOTICE_TIME = 0
FRAME_NOTICE_TEXT = None
FRAME_NOTICE_TEXT_RECOG = None

BOSS_STATUS_BOUNDING_BOX_0 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_1 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_2 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_3 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
BOSS_STATUS_BOUNDING_BOX_4 = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}

DISCONNECT_DIALOG_BOUNDING_BOX = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
FRAME_DISCONNECT_DIALOG = None

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
    'phreeoni',
    'mistress',
    'kraken',
    'eddga',
    'maya',
    'pharaoh',
    'orc hero',
    'hero',
    'orc Lord',
    'lord',
    'eclipse',
    'mastering',
    'ghosting',
    'ghost',
    'toad',
    'dragon fly',
    'dragon',
    'fly',
    'king dramoh',
    'king',
    'dramoh',
    'angeling',
    'angel',
    'deviling',
    'devil',
]

SPAWNED_TIME = {
    # MVP
    'phreeoni': 0,
    'mistress': 0,
    'kraken': 0,
    'eddga': 0,
    'orchero': 0,
    'maya': 0,
    'pharaoh': 0,
    'orclord': 0,
    # MINI
    'eclipse': 0,
    'dragonfly': 0,
    'mastering': 0,
    'ghosting': 0,
    'kingdramoh': 0,
    'toad': 0,
    'angeling': 0,
    'deviling': 0,
}

BOSS_DATAS = {
    # MVP
    "phreeoni": {
        "fullName": "Phreeoni",
        "name": "phreeoni",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30008.9a7d59be.png",
        "type": "MVP",
        "isAlive": False,
    },
    "mistress": {
        "fullName": "Mistress",
        "name": "mistress",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30007.90897e7b.png",
        "type": "MVP",
        "isAlive": False,
    },
    "kraken": {
        "fullName": "Kraken",
        "name": "kraken",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30023.172d6779.png",
        "type": "MVP",
        "isAlive": False,
    },
    "eddga": {
        "fullName": "Eddga",
        "name": "eddga",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30010.d2e4ff07.png",
        "type": "MVP",
        "isAlive": False,
    },
    "orchero": {
        "fullName": "Orc Hero",
        "name": "orchero",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30012.7543c88a.png",
        "type": "MVP",
        "isAlive": False,
    },
    "maya": {
        "fullName": "Maya",
        "name": "maya",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30009.36df383f.png",
        "type": "MVP",
        "isAlive": False,
    },
    "pharaoh": {
        "fullName": "Pharaoh",
        "name": "pharaoh",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30017.158c2197.png",
        "type": "MVP",
        "isAlive": False,
    },
    "orclord": {
        "fullName": "Orc Lord",
        "name": "orclord",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30015.f8302e27.png",
        "type": "MVP",
        "isAlive": False,
    },
    # MINI
    "eclipse": {
        "fullName": "Eclipse",
        "name": "eclipse",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/31006.c8c5eef9.png",
        "type": "Miniboss",
        "isAlive": False,
    },
    "dragonfly": {
        "fullName": "Dragon Fly",
        "name": "dragonfly",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/31004.fca89f61.png",
        "type": "Miniboss",
        "isAlive": False,
    },
    "mastering": {
        "fullName": "Mastering",
        "name": "mastering",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/31002.9f826602.png",
        "type": "Miniboss",
        "isAlive": False,
    },
    "ghosting": {
        "fullName": "Ghosting",
        "name": "ghosting",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/31008.e6e0d610.png",
        "type": "Miniboss",
        "isAlive": False,
    },
    "kingdramoh": {
        "fullName": "King Dramoh",
        "name": "kingdramoh",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/31009.aaf00d72.png",
        "type": "Miniboss",
        "isAlive": False,
    },
    "toad": {
        "fullName": "Toad",
        "name": "toad",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/31001.f1f2afb9.png",
        "type": "Miniboss",
        "isAlive": False,
    },
    "angeling": {
        "fullName": "Angeling",
        "name": "angeling",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30001.32d166a9.png",
        "type": "Miniboss",
        "isAlive": False,
    },
    "deviling": {
        "fullName": "Deviling",
        "name": "deviling",
        "thumbnailUrl": "https://sf16-g-alisg.dailygn.com/obj/g-marketing-assets-sg/static/media/30003.a217d20e.png",
        "type": "Miniboss",
        "isAlive": False,
    },
}
