# -*- coding: utf-8 -*-
import config

from repositories import func_repo
from repositories import detector_repo
from repositories import webhook_repo

CHECKING_COOLDOWN = 900


def spawn_detecting(boss_data, bounding_area):
    # Get bounding frame
    frame = func_repo.get_bounding_frame(config.SCREENSHOT, bounding_area)
    # Checking green background
    if detector_repo.detect_green_color(frame):
        webhook_repo.send_message_webhook(
            'spawned', {"boss_data": boss_data})
        config.SPAWNED_TIME[boss_data["name"]] = config.CURRENT_TIME
        config.BOSS_DATAS[boss_data["name"]]["isAlive"] = True


def dead_detecting(boss_data, bounding_area):
    # Get bounding frame
    frame = func_repo.get_bounding_frame(config.SCREENSHOT, bounding_area)
    # Checking green background
    if config.BOSS_DATAS[boss_data["name"]]["isAlive"] and detector_repo.detect_green_color(frame) is False:
        webhook_repo.send_message_webhook(
            'dead', {"boss_data": boss_data})
        config.SPAWNED_TIME[boss_data["name"]] = config.CURRENT_TIME
        config.BOSS_DATAS[boss_data["name"]]["isAlive"] = False


def checking_box_1(name):
    # Checking process
    if config.CURRENT_TIME > (config.SPAWNED_TIME[name] + CHECKING_COOLDOWN):
        # Get boss data
        boss_data = config.BOSS_DATAS[name]
        spawn_detecting(boss_data, config.BOSS_STATUS_BOUNDING_BOX_1)


def checking_box_2(name):
    # Checking process
    if config.CURRENT_TIME > (config.SPAWNED_TIME[name] + CHECKING_COOLDOWN):
        # Get boss data
        boss_data = config.BOSS_DATAS[name]
        spawn_detecting(boss_data, config.BOSS_STATUS_BOUNDING_BOX_2)
    dead_detecting(boss_data, config.BOSS_STATUS_BOUNDING_BOX_2)


def checking_box_3(name):
    # Checking process
    if config.CURRENT_TIME > (config.SPAWNED_TIME[name] + CHECKING_COOLDOWN):
        # Get boss data
        boss_data = config.BOSS_DATAS[name]
        spawn_detecting(boss_data, config.BOSS_STATUS_BOUNDING_BOX_3)


def checking_box_4(name):
    # Checking process
    if config.CURRENT_TIME > (config.SPAWNED_TIME[name] + CHECKING_COOLDOWN):
        # Get boss data
        boss_data = config.BOSS_DATAS[name]
        spawn_detecting(boss_data, config.BOSS_STATUS_BOUNDING_BOX_4)
