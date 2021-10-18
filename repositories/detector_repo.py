# -*- coding: utf-8 -*-
import config

import sys
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
    print("[SYSTEM]: Bot started!")
    webhook_repo.send_message_webhook('bot_start', {})

    while config.IS_RUNNING:
        if config.IS_HOLD is False:
            # Set current time
            config.CURRENT_TIME = time.time()

            # Crop the emulator screenshot
            func_repo.get_emulator_screenshot()

            # Initialize and render bounding
            render_repo.render_notice_bounding()
            render_repo.render_mvp_tab_bounding()
            render_repo.render_boss_status_bounding()
            render_repo.render_disconnect_dialog_bounding()

            # Core Detection
            disconnect_detector()
            game_failed_detector()
            anounce_detector()
            boss_detector()

            # Render
            render_repo.show()

    # Send shutting down message
    webhook_repo.send_message_webhook('bot_stop', {})


def disconnect_detector():
    config.FRAME_DISCONNECT_DIALOG = func_repo.get_bounding_frame(
        config.DISCONNECT_DIALOG_BOUNDING_BOX)
    hsv_frame = cv2.cvtColor(
        np.array(config.FRAME_DISCONNECT_DIALOG), cv2.COLOR_BGR2HSV)
    if detect_white_color(hsv_frame):
        # Send disconnect message
        print('[ERROR]: The game has disconnected.')
        webhook_repo.send_message_webhook('disconnect', {})
        config.IS_RUNNING = False
        sys.exit()


def game_failed_detector():
    config.FRAME_DISCONNECT_DIALOG = func_repo.get_bounding_frame(
        config.BOSS_STATUS_BOUNDING_BOX_3)
    hsv_frame = cv2.cvtColor(
        np.array(config.FRAME_DISCONNECT_DIALOG), cv2.COLOR_BGR2HSV)
    if detect_gray_color(hsv_frame):
        # Send disconnect message
        print('[ERROR]: The game crashed exit.')
        webhook_repo.send_message_webhook('error', {"reason": "Game crashed"})
        config.IS_RUNNING = False
        sys.exit()


def anounce_detector():
    config.FRAME_NOTICE_TEXT = func_repo.get_bounding_frame(
        config.NOTICE_BOUNDING_BOX)
    config.FRAME_NOTICE_TEXT_RECOG = recognition_repo.blackwhite_image_processing(
        config.FRAME_NOTICE_TEXT)
    recognition_repo.refreshing_text_detector(config.FRAME_NOTICE_TEXT_RECOG)


def boss_detector():
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
            thread1 = Thread(
                target=boss_tracker_repo.checking_box_1('phreeoni'))
            thread2 = Thread(
                target=boss_tracker_repo.checking_box_2('mistress'))
            thread3 = Thread(target=boss_tracker_repo.checking_box_3('kraken'))
            thread4 = Thread(target=boss_tracker_repo.checking_box_4('eddga'))
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
        elif setNumber == 2:  # [orchero maya pharaoh orclord]
            thread1 = Thread(
                target=boss_tracker_repo.checking_box_1('orchero'))
            thread2 = Thread(target=boss_tracker_repo.checking_box_2('maya'))
            thread3 = Thread(
                target=boss_tracker_repo.checking_box_3('pharaoh'))
            thread4 = Thread(
                target=boss_tracker_repo.checking_box_4('orclord'))
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
    if bossType == 'mini':
        if setNumber == 1:  # [eclipse dragonfly mastering ghosting]
            thread1 = Thread(
                target=boss_tracker_repo.checking_box_1('eclipse'))
            thread2 = Thread(
                target=boss_tracker_repo.checking_box_2('dragonfly'))
            thread3 = Thread(
                target=boss_tracker_repo.checking_box_3('mastering'))
            thread4 = Thread(
                target=boss_tracker_repo.checking_box_4('ghosting'))
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
        elif setNumber == 2:  # [kingdramoh toad angeling deviling]
            thread1 = Thread(
                target=boss_tracker_repo.checking_box_1('kingdramoh'))
            thread2 = Thread(target=boss_tracker_repo.checking_box_2('toad'))
            thread3 = Thread(
                target=boss_tracker_repo.checking_box_3('angeling'))
            thread4 = Thread(
                target=boss_tracker_repo.checking_box_4('deviling'))
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()


def detect_white_color(hsv_frame):
    low_white = np.array([100, 0, 200])
    high_white = np.array([125, 40, 255])
    mask1 = cv2.inRange(hsv_frame, low_white, high_white)
    mask2 = cv2.inRange(hsv_frame, low_white, high_white)
    mask = cv2.bitwise_or(mask1, mask2)
    # Checking
    if cv2.countNonZero(mask) > 0:  # ขาวแล้ว
        return True
    else:
        return False


def detect_gray_color(hsv_frame):
    low_white = np.array([100, 0, 10])
    high_white = np.array([125, 40, 100])
    mask1 = cv2.inRange(hsv_frame, low_white, high_white)
    mask2 = cv2.inRange(hsv_frame, low_white, high_white)
    mask = cv2.bitwise_or(mask1, mask2)
    # Checking
    if cv2.countNonZero(mask) > 0:  # ขาวแล้ว
        return True
    else:
        return False


def detect_green_color(hsv_frame):
    low_green = np.array([45, 40, 50])
    high_green = np.array([65, 255, 255])
    mask1 = cv2.inRange(hsv_frame, low_green, high_green)
    mask2 = cv2.inRange(hsv_frame, low_green, high_green)
    mask = cv2.bitwise_or(mask1, mask2)
    # Checking
    if cv2.countNonZero(mask) > 0:  # เขียวแล้ว
        return True
    else:
        return False
