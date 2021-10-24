# -*- coding: utf-8 -*-
import config

import sys
import cv2
import numpy as np
import time
import mss
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

    thread1 = Thread(target=game_failed_detector)
    thread2 = Thread(target=disconnect_detector)
    thread3 = Thread(target=boss_detector)
    thread4 = Thread(target=anounce_detector)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # Send shutting down message
    webhook_repo.send_message_webhook('bot_stop', {})
    sys.exit()


def disconnect_detector():
    self_screenshot = mss.mss()
    while config.IS_RUNNING:
        time.sleep(1.0)  # Delay 1000 milliseconds
        if config.IS_HOLD is False and config.IS_DISCONNECTED is False and config.IS_CRASHED is False:
            # Set current time
            config.CURRENT_TIME = time.time()
            # Crop the emulator screenshot
            func_repo.get_emulator_screenshot(self_screenshot)
            # Initialize and render bounding
            render_repo.render_disconnect_dialog_bounding()
            # Process
            config.FRAME_DISCONNECT_DIALOG = func_repo.get_bounding_frame(
                self_screenshot, config.DISCONNECT_DIALOG_BOUNDING_BOX)
            if config.FRAME_DISCONNECT_DIALOG is not None:
                hsv_frame = cv2.cvtColor(
                    np.array(config.FRAME_DISCONNECT_DIALOG), cv2.COLOR_BGR2HSV)
                if detect_color(hsv_frame, [100, 0, 200], [125, 40, 255]):
                    # Send disconnect message
                    print('[ERROR]: The game has disconnected.')
                    webhook_repo.send_message_webhook('disconnect', {})
                    config.IS_RUNNING = False
                    sys.exit()
    sys.exit()


def game_failed_detector():
    self_screenshot = mss.mss()
    while config.IS_RUNNING:
        time.sleep(1.0)  # Delay 1000 milliseconds
        if config.IS_HOLD is False and config.IS_DISCONNECTED is False and config.IS_CRASHED is False:
            # Set current time
            config.CURRENT_TIME = time.time()
            # Crop the emulator screenshot
            func_repo.get_emulator_screenshot(self_screenshot)
            # Initialize and render bounding
            render_repo.render_boss_status_bounding()  # using BOSS_STATUS_BOUNDING_BOX_3
            config.FRAME_DISCONNECT_DIALOG = func_repo.get_bounding_frame(
                self_screenshot, config.BOSS_STATUS_BOUNDING_BOX_3)
            if config.FRAME_DISCONNECT_DIALOG is not None:
                hsv_frame = cv2.cvtColor(
                    np.array(config.FRAME_DISCONNECT_DIALOG), cv2.COLOR_BGR2HSV)
                if detect_color(hsv_frame, [100, 0, 10], [125, 40, 100]):
                    # Send disconnect message
                    print('[ERROR]: The game crashed exit.')
                    webhook_repo.send_message_webhook(
                        'error', {"reason": "Game crashed"})
                    config.IS_RUNNING = False
                    sys.exit()
    sys.exit()


def anounce_detector():
    self_screenshot = mss.mss()
    while config.IS_RUNNING:
        time.sleep(0.25)  # Delay 250 milliseconds
        if config.IS_HOLD is False and config.IS_DISCONNECTED is False and config.IS_CRASHED is False:
            # Set current time
            config.CURRENT_TIME = time.time()
            # Crop the emulator screenshot
            func_repo.get_emulator_screenshot(self_screenshot)
            # Initialize and render bounding
            render_repo.render_notice_bounding()
            # Process
            config.FRAME_NOTICE_TEXT = func_repo.get_bounding_frame(
                self_screenshot, config.NOTICE_BOUNDING_BOX)
            if config.FRAME_NOTICE_TEXT is not None:
                config.FRAME_NOTICE_TEXT_RECOG = recognition_repo.blackwhite_image_processing(
                    config.FRAME_NOTICE_TEXT)
                recognition_repo.refreshing_text_detector(
                    config.FRAME_NOTICE_TEXT_RECOG)
    sys.exit()


def boss_detector():
    self_screenshot = mss.mss()
    while config.IS_RUNNING:
        if config.IS_HOLD is False and config.IS_DISCONNECTED is False and config.IS_CRASHED is False:
            # Set current time
            config.CURRENT_TIME = time.time()
            # Crop the emulator screenshot
            func_repo.get_emulator_screenshot(self_screenshot)
            # Initialize and render bounding
            render_repo.render_mvp_tab_bounding()
            render_repo.render_boss_status_bounding()
            # MVP Step
            func_repo.mouse_click_mvp_tab()
            boss_status_detector(self_screenshot, 'mvp', 1)
            func_repo.mouse_draging()
            boss_status_detector(self_screenshot, 'mvp', 2)
            # MINI Step
            func_repo.mouse_click_mini_tab()
            boss_status_detector(self_screenshot, 'mini', 1)
            func_repo.mouse_draging()
            boss_status_detector(self_screenshot, 'mini', 2)
    sys.exit()


def boss_status_detector(sct, bossType, setNumber):
    if config.IS_HOLD is False and config.IS_DISCONNECTED is False and config.IS_CRASHED is False:
        if bossType == 'mvp':
            if setNumber == 1:  # [phreeoni mistress kraken eddga]
                boss_tracker_repo.checking_box_1(sct, 'phreeoni')
                boss_tracker_repo.checking_box_2(sct, 'mistress')
                boss_tracker_repo.checking_box_3(sct, 'kraken')
                boss_tracker_repo.checking_box_4(sct, 'eddga')
            elif setNumber == 2:  # [orchero maya pharaoh orclord]
                boss_tracker_repo.checking_box_1(sct, 'orchero')
                boss_tracker_repo.checking_box_2(sct, 'maya')
                boss_tracker_repo.checking_box_3(sct, 'pharaoh')
                boss_tracker_repo.checking_box_4(sct, 'orclord')
        if bossType == 'mini':
            if setNumber == 1:  # [eclipse dragonfly mastering ghosting]
                boss_tracker_repo.checking_box_1(sct, 'eclipse')
                boss_tracker_repo.checking_box_2(sct, 'dragonfly')
                boss_tracker_repo.checking_box_3(sct, 'mastering')
                boss_tracker_repo.checking_box_4(sct, 'ghosting')
            elif setNumber == 2:  # [kingdramoh toad angeling deviling]
                boss_tracker_repo.checking_box_1(sct, 'kingdramoh')
                boss_tracker_repo.checking_box_2(sct, 'toad')
                boss_tracker_repo.checking_box_3(sct, 'angeling')
                boss_tracker_repo.checking_box_4(sct, 'deviling')


def detect_color(hsv_frame, low_color, high_color):
    mask1 = cv2.inRange(hsv_frame, low_color, high_color)
    mask2 = cv2.inRange(hsv_frame, low_color, high_color)
    mask = cv2.bitwise_or(mask1, mask2)
    # Checking
    if cv2.countNonZero(mask) > 0:
        return True
    else:
        return False
