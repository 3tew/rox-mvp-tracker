import config
import cv2
import numpy as np

from repositories import func_repo
from repositories import detector_repo


# MVP Set 1 ===================================================
def phreeoni_checking():
    boss_name = 'Phreeoni'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["phreeoni"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_1 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_1)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_1['rgb'], config.FRAME_BOSS_STATUS_BOX_1['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["phreeoni"] = config.CURRENT_TIME


def mistress_checking():
    boss_name = 'Mistress'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["mistress"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_2 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_2)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_2['rgb'], config.FRAME_BOSS_STATUS_BOX_2['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["mistress"] = config.CURRENT_TIME


def kraken_checking():
    boss_name = 'Kraken'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["kraken"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_3 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_3)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_3['rgb'], config.FRAME_BOSS_STATUS_BOX_3['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["kraken"] = config.CURRENT_TIME


def eddga_checking():
    boss_name = 'Eddga'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["eddga"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_4 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_4)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_4['rgb'], config.FRAME_BOSS_STATUS_BOX_4['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["eddga"] = config.CURRENT_TIME


# MVP Set 2 ===================================================
def orchero_checking():
    boss_name = 'Orc Hero'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["orchero"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_1 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_1)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_1['rgb'], config.FRAME_BOSS_STATUS_BOX_1['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["orchero"] = config.CURRENT_TIME


def maya_checking():
    boss_name = 'Maya'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["maya"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_2 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_2)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_2['rgb'], config.FRAME_BOSS_STATUS_BOX_2['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["maya"] = config.CURRENT_TIME


def pharaoh_checking():
    boss_name = 'Pharoah'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["pharaoh"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_3 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_3)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_3['rgb'], config.FRAME_BOSS_STATUS_BOX_3['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["pharaoh"] = config.CURRENT_TIME


def orclord_checking():
    boss_name = 'Orc Lord'
    if config.CURRENT_TIME > (config.MVP_SPAWNED_TIME["orclord"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_4 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_4)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_4['rgb'], config.FRAME_BOSS_STATUS_BOX_4['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MVP_SPAWNED_TIME["orclord"] = config.CURRENT_TIME


# MINI Set 1 ===================================================
def eclipse_checking():
    boss_name = 'Eclipse'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["eclipse"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_1 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_1)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_1['rgb'], config.FRAME_BOSS_STATUS_BOX_1['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["eclipse"] = config.CURRENT_TIME


def dragonfly_checking():
    boss_name = 'Dragon Fly'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["dragonfly"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_2 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_2)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_2['rgb'], config.FRAME_BOSS_STATUS_BOX_2['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["dragonfly"] = config.CURRENT_TIME


def mastering_checking():
    boss_name = 'Mastering'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["mastering"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_3 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_3)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_3['rgb'], config.FRAME_BOSS_STATUS_BOX_3['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["mastering"] = config.CURRENT_TIME


def ghosting_checking():
    boss_name = 'Ghosting'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["ghosting"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_4 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_4)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_4['rgb'], config.FRAME_BOSS_STATUS_BOX_4['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["ghosting"] = config.CURRENT_TIME


# MINI Set 2 ===================================================
def kingdramoh_checking():
    boss_name = 'King Dramoh'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["kingdramoh"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_1 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_1)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_1['rgb'], config.FRAME_BOSS_STATUS_BOX_1['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["kingdramoh"] = config.CURRENT_TIME


def toad_checking():
    boss_name = 'Toad'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["toad"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_2 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_2)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_2['rgb'], config.FRAME_BOSS_STATUS_BOX_2['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["toad"] = config.CURRENT_TIME


def angeling_checking():
    boss_name = 'Angeling'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["angeling"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_3 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_3)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_3['rgb'], config.FRAME_BOSS_STATUS_BOX_3['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["angeling"] = config.CURRENT_TIME


def deviling_checking():
    boss_name = 'Deviling'
    if config.CURRENT_TIME > (config.MINI_SPAWNED_TIME["deviling"] + 900):
        # Get bounding frame
        config.FRAME_BOSS_STATUS_BOX_4 = func_repo.get_bounding_frame(
            config.BOSS_STATUS_BOUNDING_BOX_4)
        # Checking green background
        if detector_repo.detect_green_color(config.FRAME_BOSS_STATUS_BOX_4['rgb'], config.FRAME_BOSS_STATUS_BOX_4['hsv']):
            detector_repo.send_message_webhook(boss_name, 'spawned')
            config.MINI_SPAWNED_TIME["deviling"] = config.CURRENT_TIME
