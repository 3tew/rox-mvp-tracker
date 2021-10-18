# -*- coding: utf-8 -*-
import config

import requests
from threading import Thread
from datetime import datetime


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
        data = refreshing_message_case(
            options["boss_data"], options["is_abyss"], strTime, data)
    elif case == 'spawned':
        data = spawned_message_case(options["boss_data"], strTime, data)
    elif case == 'bot_start':
        data = bot_start_message_case(data)
    elif case == 'bot_stop':
        data = bot_stop_message_case(data)
    elif case == 'error':
        data = error_message_case(data, options["reason"])
    elif case == 'disconnect':
        data = disconnect_message_case(data)

    # sending get request and saving the response as response object
    for url in config.DISCORD_WEBHOOK_URLS:
        thread = Thread(target=request_discord_webhook(url, data))
        thread.start()


def refreshing_message_case(boss_data, isAbyss, strTime, data):
    data['username'] = 'ROX - MVP Announcer'
    data['embeds'][0]['color'] = 65504  # Blue
    data['embeds'][0]['title'] = '📢 ' + \
        ('Abyss ' + boss_data['fullName']) if isAbyss else (boss_data['fullName']) + \
        (" `Development`" if config.IS_DEVELOPMENT else "")
    data['embeds'][0]['description'] = \
        '[' + boss_data['type'] + '] กำลังจะรีเฟรช... (ประกาศแล้ว)'
    data['embeds'][0]['thumbnail']['url'] = boss_data['thumbnailUrl']

    config.NOTICE_TIME = config.CURRENT_TIME
    print('[' + strTime + '] ' + boss_data['fullName'] + ' is refreshing...')
    return data


def spawned_message_case(boss_data, strTime, data):
    data['username'] = 'ROX - MVP Tracker'
    data['embeds'][0]['color'] = 1376000  # Green
    data['embeds'][0]['title'] = boss_data['fullName'] + \
        (" `Development`" if config.IS_DEVELOPMENT else "")
    data['embeds'][0]['description'] = \
        '[' + boss_data['type'] + '] ปรากฏแล้ว!'
    data['embeds'][0]['thumbnail']['url'] = boss_data['thumbnailUrl']

    print('[' + strTime + '] ' + boss_data['fullName'] + ' spawned!')
    return data


def bot_start_message_case(data):
    data['embeds'][0]['color'] = 16771928  # Yellow
    data['embeds'][0]['title'] = 'Bot started' + \
        (" `Development`" if config.IS_DEVELOPMENT else "")
    data['embeds'][0]['description'] = \
        'บอทเริ่มทำงาน\n\n✅ MVP Spawn Tracker\n✅ MVP Refreshing Detector'
    return data


def bot_stop_message_case(data):
    data['embeds'][0]['color'] = 16711680  # Red
    data['embeds'][0]['title'] = 'Bot is shutting down' + \
        (" `Development`" if config.IS_DEVELOPMENT else "")
    data['embeds'][0]['description'] = 'กำลังปิดการทำงาน'
    return data


def error_message_case(data, reason=""):
    data['embeds'][0]['color'] = 16711680  # Red
    data['embeds'][0]['title'] = 'Something wrong' + \
        (" `Development`" if config.IS_DEVELOPMENT else "")
    data['embeds'][0]['description'] = 'เกิดข้อผิดพลาด, กำลังปิดการทำงาน' + \
        (' *(' + reason + ')*'if len(reason) > 0 else "")
    return data


def disconnect_message_case(data):
    data['embeds'][0]['color'] = 16711680  # Red
    data['embeds'][0]['title'] = 'Disconnected' + \
        (" `Development`" if config.IS_DEVELOPMENT else "")
    data['embeds'][0]['description'] = 'บอทถูกตัดการเชื่อมต่อ'
    return data


def request_discord_webhook(url, data):
    result = requests.post(url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("[WEBHOOK]: ErrorException, " + err)
    else:
        print("[SYSTEM]: Payload delivered successfully, code {}.".format(
            result.status_code))
