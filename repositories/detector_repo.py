import config

import cv2
import numpy as np
import time
from threading import Thread

from repositories import func_repo
from repositories import render_repo
from repositories import recognition_repo
from repositories import boss_tracker_repo
from repositories import webhook_repo


def running():
    # Send started message
    webhook_repo.send_message_webhook('bot_start', {})

    while config.IS_RUNNING:
        # Set current time
        config.CURRENT_TIME = time.time()

        # Crop the emulator screenshot
        func_repo.get_emulator_screenshot()

        # Initialize and render bounding
        render_repo.render_notice_bounding()
        render_repo.render_mvp_tab_bounding()
        render_repo.render_boss_status_bounding()

        ### Core Detection
        # boss_anounce_detector()
        boss_tracking()

        ### Render infos
        # render_repo.show() # Uncomment for debugging


def boss_anounce_detector():
    config.FRAME_NOTICE_TEXT = func_repo.get_bounding_frame(config.NOTICE_BOUNDING_BOX)
    config.FRAME_NOTICE_TEXT_RECOG = recognition_repo.blackwhite_image_processing(config.FRAME_NOTICE_TEXT)
    recognition_repo.refreshing_text_detector(config.FRAME_NOTICE_TEXT_RECOG)


def boss_tracking():
    # MVP Step
    func_repo.mouse_click_mvp_tab()
    boss_status_detector('mvp', 1)
    func_repo.mouse_draging()
    boss_status_detector('mvp', 2)
    # MINI Step
    func_repo.mouse_click_mini_tab()
    boss_status_detector('mini', 1)
    func_repo.mouse_draging()
    boss_status_detector('mini', 2)


def boss_status_detector(bossType, setNumber):
    if bossType == 'mvp':
        if setNumber == 1:  # [phreeoni mistress kraken eddga]
            thread1 = Thread(target=boss_tracker_repo.checking_box_1('phreeoni'))
            thread2 = Thread(target=boss_tracker_repo.checking_box_2('mistress'))
            thread3 = Thread(target=boss_tracker_repo.checking_box_3('kraken'))
            thread4 = Thread(target=boss_tracker_repo.checking_box_4('eddga'))
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
        elif setNumber == 2:  # [orchero maya pharaoh orclord]
            thread1 = Thread(target=boss_tracker_repo.checking_box_1('orchero'))
            thread2 = Thread(target=boss_tracker_repo.checking_box_2('maya'))
            thread3 = Thread(target=boss_tracker_repo.checking_box_3('pharaoh'))
            thread4 = Thread(target=boss_tracker_repo.checking_box_4('orclord'))
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
    if bossType == 'mini':
        if setNumber == 1:  # [eclipse dragonfly mastering ghosting]
            thread1 = Thread(target=boss_tracker_repo.checking_box_1('eclipse'))
            thread2 = Thread(target=boss_tracker_repo.checking_box_2('dragonfly'))
            thread3 = Thread(target=boss_tracker_repo.checking_box_3('mastering'))
            thread4 = Thread(target=boss_tracker_repo.checking_box_4('ghosting'))
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
        elif setNumber == 2:  # [kingdramoh toad angeling deviling]
            thread1 = Thread(target=boss_tracker_repo.checking_box_1('kingdramoh'))
            thread2 = Thread(target=boss_tracker_repo.checking_box_2('toad'))
            thread3 = Thread(target=boss_tracker_repo.checking_box_3('angeling'))
            thread4 = Thread(target=boss_tracker_repo.checking_box_4('deviling'))
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
