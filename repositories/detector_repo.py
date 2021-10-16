import config

import cv2
import numpy as np
import requests
import time
from threading import Thread
from datetime import datetime

from repositories import func_repo
from repositories import render_repo
from repositories import recognition_repo
from repositories import boss_tracker_repo
from repositories import detector_repo


def running():
    # Send started message
    detector_repo.send_message_webhook('bot_start', {})

    while config.IS_RUNNING:
        # Set current time
        config.CURRENT_TIME = time.time()

        # Crop the emulator screenshot
        func_repo.get_emulator_screenshot()

        # Initialize and render bounding
        render_repo.render_notice_bounding()
        render_repo.render_mvp_tab_bounding()
        render_repo.render_boss_status_bounding()

        # Core Detection
        # boss_anounce_detector()
        boss_tracking()

        # Render infos
        # render_repo.show() # Comment for optimize process


def boss_anounce_detector():
    func_repo.crop_boss_notice_frame(config.NOTICE_BOUNDING_BOX)
    recognition_repo.refreshing_text_detector()


def boss_tracking():
    # Steps
    func_repo.mouse_click_mvp_tab()
    boss_status_detector('mvp', 1)
    func_repo.mouse_draging()
    boss_status_detector('mvp', 2)
    func_repo.mouse_click_mini_tab()
    boss_status_detector('mini', 1)
    func_repo.mouse_draging()
    boss_status_detector('mini', 2)


def boss_status_detector(bossType, setNumber):
    if bossType == 'mvp':
        if setNumber == 1:  # [phreeoni mistress kraken eddga]
            thread1 = Thread(target=boss_tracker_repo.phreeoni_checking())
            thread2 = Thread(target=boss_tracker_repo.mistress_checking())
            thread3 = Thread(target=boss_tracker_repo.kraken_checking())
            thread4 = Thread(target=boss_tracker_repo.eddga_checking())
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
        elif setNumber == 2:  # [orchero maya pharaoh orclord]
            thread1 = Thread(target=boss_tracker_repo.orchero_checking())
            thread2 = Thread(target=boss_tracker_repo.maya_checking())
            thread3 = Thread(target=boss_tracker_repo.pharaoh_checking())
            thread4 = Thread(target=boss_tracker_repo.orclord_checking())
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
    if bossType == 'mini':
        if setNumber == 1:  # [eclipse dragonfly mastering ghosting]
            thread1 = Thread(target=boss_tracker_repo.eclipse_checking())
            thread2 = Thread(target=boss_tracker_repo.dragonfly_checking())
            thread3 = Thread(target=boss_tracker_repo.mastering_checking())
            thread4 = Thread(target=boss_tracker_repo.ghosting_checking())
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
        elif setNumber == 2:  # [kingdramoh toad angeling deviling]
            thread1 = Thread(target=boss_tracker_repo.kingdramoh_checking())
            thread2 = Thread(target=boss_tracker_repo.toad_checking())
            thread3 = Thread(target=boss_tracker_repo.angeling_checking())
            thread4 = Thread(target=boss_tracker_repo.deviling_checking())
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()


def detect_green_color(hsv_frame):
    low_green = np.array([40, 40, 40])
    high_green = np.array([70, 255, 255])
    mask1 = cv2.inRange(hsv_frame, low_green, high_green)
    mask2 = cv2.inRange(hsv_frame, low_green, high_green)
    mask = cv2.bitwise_or(mask1, mask2)
    # Checking
    if cv2.countNonZero(mask) > 0:  # เขียวแล้ว
        return True
    else:
        return False


def send_message_webhook(case, options):
    now = datetime.now()
    strTime = now.strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "content": "",
        "username": "ROX - MVP Bot",
        "embeds": [
            {
                "title": "",
                "description": "",
                "color": 16734296,
                "footer": {
                    "text": "Develop by (fb.com/thanatos1995) • " + strTime,
                    "icon_url": "https://lh3.googleusercontent.com/-jzKuCLruWuE/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucm5SxfcaJKzVr1kj9hGwC7EgmC5QQ/photo.jpg",
                },
                "thumbnail": {
                    "url": "",
                },
            },
        ],
    }

    if case == 'refreshing':
        data = refreshing_message_case(options["boss_data"], strTime, data)
    elif case == 'spawned':
        data = spawned_message_case(options["boss_data"], strTime, data)
    elif case == 'bot_start':
        data = bot_start_message_case(data)
    elif case == 'bot_stop':
        data = bot_stop_message_case(data)

    # sending get request and saving the response as response object
    for url in config.DISCORD_WEBHOOK_URLS:
        thread = Thread(target=request_discord_webhook(url, data))
        thread.start()


def refreshing_message_case(boss_data, strTime, data):
    data['username'] = 'ROX - MVP Announcer'
    data['embeds'][0]['color'] = 65504  # Blue
    data['embeds'][0]['title'] = boss_data['fullName']
    data['embeds'][0]['description'] = \
        '[' + boss_data['type'] + '] กำลังจะรีเฟรช... (ประกาศ)'
    data['embeds'][0]['thumbnail']['url'] = \
        '[' + boss_data['thumbnailUrl']

    config.NOTICE_TIME = config.CURRENT_TIME
    print('[' + strTime + '] ' + boss_data['fullName'] + ' is refreshing...')
    return data


def spawned_message_case(boss_data, strTime, data):
    data['username'] = 'ROX - MVP Tracker'
    data['embeds'][0]['color'] = 1376000  # Green
    data['embeds'][0]['title'] = boss_data['fullName']
    data['embeds'][0]['description'] = \
        '[' + boss_data['type'] + '] ปรากฏแล้ว!'
    data['embeds'][0]['thumbnail']['url'] = boss_data['thumbnailUrl']

    print('[' + strTime + '] ' + boss_data['fullName'] + ' spawned!')
    return data


def bot_start_message_case(data):
    data['embeds'][0]['color'] = 16771928  # Yellow
    data['embeds'][0]['title'] = 'Bot started'
    data['embeds'][0]['description'] = \
        'บอทเริ่มทำงาน\n\n✅ MVP Spawn Tracker\n❌ MVP Refreshing Detector *(กำลังทำ)*'
    return data


def bot_stop_message_case(data):
    data['embeds'][0]['color'] = 16711680  # Red
    data['embeds'][0]['title'] = 'Bot shutting down'
    data['embeds'][0]['description'] = 'กำลังปิดการทำงาน'
    return data


def request_discord_webhook(url, data):
    result = requests.post(url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(
            result.status_code))
