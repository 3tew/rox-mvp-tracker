import config

import os
import sys
import pyautogui
import pygetwindow
import re
import cv2
import numpy as np
import requests
import base64
from PIL import Image
from time import gmtime, strftime
from threading import Thread

from repositories import func_repo
from repositories import recognition_repo
from repositories import boss_tracker_repo


def running_step():
    # Start thread
    # thread1 = Thread(target=boss_anounce_detector)
    thread2 = Thread(target=boss_tracking)
    # thread1.start()
    thread2.start()
    # thread1.join()
    thread2.join()


def boss_anounce_detector():
    func_repo.crop_boss_notice_frame(config.NOTICE_BOUNDING_BOX)
    recognition_repo.refreshing_text_detector()


def boss_tracking():
    # disable this fail-safe (for multiple display monitor)
    pyautogui.FAILSAFE = False
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
            boss_tracker_repo.phreeoni_checking()
            boss_tracker_repo.mistress_checking()
            boss_tracker_repo.kraken_checking()
            boss_tracker_repo.eddga_checking()
        elif setNumber == 2:  # [orchero maya pharaoh orclord]
            boss_tracker_repo.orchero_checking()
            boss_tracker_repo.maya_checking()
            boss_tracker_repo.pharaoh_checking()
            boss_tracker_repo.orclord_checking()
    if bossType == 'mini':
        if setNumber == 1:  # [eclipse dragonfly mastering ghosting]
            boss_tracker_repo.eclipse_checking()
            boss_tracker_repo.dragonfly_checking()
            boss_tracker_repo.mastering_checking()
            boss_tracker_repo.ghosting_checking()
        elif setNumber == 2:  # [kingdramoh toad angeling deviling]
            boss_tracker_repo.kingdramoh_checking()
            boss_tracker_repo.toad_checking()
            boss_tracker_repo.angeling_checking()
            boss_tracker_repo.deviling_checking()


def detect_green_color(rgb_frame, hsv_frame):
    low_green = np.array([40, 40, 40])
    high_green = np.array([70, 255, 255])
    mask1 = cv2.inRange(hsv_frame, low_green, high_green)
    mask2 = cv2.inRange(hsv_frame, low_green, high_green)
    mask = cv2.bitwise_or(mask1, mask2)
    green = cv2.bitwise_and(rgb_frame, rgb_frame, mask=mask)
    # Checking
    if cv2.countNonZero(mask) > 0:  # เขียวแล้ว
        return True
    else:
        return False


def send_message_webhook(boss_name, case):

    strTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    boss_name_strip = boss_name.replace(' ', '')
    boss_name_lower = boss_name_strip.lower()

    PARAMS = {
        "content": '',
        "embeds": [
            {
                "title": "",
                "description": "",
                "color": 16734296,
                "footer": {
                    "text": "Develop by fb.com/thanatos1995 • " + strTime,
                    "icon_url": "https://scontent.fbkk5-7.fna.fbcdn.net/v/t1.6435-9/67402512_2185187511591686_2859408008121679872_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=09cbfe&_nc_eui2=AeHw298dC14Pajk-Ckxi1IxM4SwswTM6WkvhLCzBMzpaSwiPsinyKzztoR_TLEMskorF02SMX3Qaa282WpffKVHE&_nc_ohc=wxF82DbcdLUAX8D-bOG&_nc_ht=scontent.fbkk5-7.fna&oh=baf525198a4f0a3437391bd17e038418&oe=618F5645"
                },
                "thumbnail": {
                    "url": ""
                }
            }
        ],
        "username": "ROX - MVP Tracker",
    }

    if case == 'refreshing':
        PARAMS['embeds']['0']['title'] = config.BOSS_DATAS[boss_name_lower]['fullName']
        PARAMS['embeds']['0']['description'] = '[' + \
            config.BOSS_DATAS[boss_name_lower]['type']+'] ประกาศแล้ว.'
        PARAMS['embeds']['0']['thumbnail']['url'] = '[' + \
            config.BOSS_DATAS[boss_name_lower]['thumbnailUrl']
        print('[' + strTime + '] ' + boss_name + ' is refreshing...')
        config.NOTICE_TIME = config.CURRENT_TIME
    elif case == 'spawned':
        PARAMS['embeds']['0']['title'] = config.BOSS_DATAS[boss_name_lower]['fullName']
        PARAMS['embeds']['0']['description'] = '[' + \
            config.BOSS_DATAS[boss_name_lower]['type']+'] ปรากฏแล้ว.'
        PARAMS['embeds']['0']['thumbnail']['url'] = '[' + \
            config.BOSS_DATAS[boss_name_lower]['thumbnailUrl']
        print('[' + strTime + '] ' + boss_name + ' spawned!')

    # sending get request and saving the response as response object
    for url in config.DISCORD_WEBHOOK_URLS:
        requests.post(url, json=PARAMS)
