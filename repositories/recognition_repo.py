# -*- coding: utf-8 -*-
import config

import os
import cv2
import numpy as np
import pytesseract

from repositories import webhook_repo

if os.name in ('nt', 'dos'):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def refreshing_text_detector(frame):
    # Text recognition process...
    text = pytesseract.image_to_string(frame)

    text = text.strip()
    text = text.lower()

    if config.IS_DEVELOPMENT and (len(text) > 0):
        print("[SYSTEM]: Text = '" + text + "'")  # Debugging

    for boss_name in config.BOSS_NAMES:
        # ระยะเวลาระหว่างประกาศ 30 วินาที
        if (boss_name in text) and (config.CURRENT_TIME - config.NOTICE_TIME) > 30:
            # Checking Abyss type
            isAbyss = True if ('abyss' in text) else False
            # MVP
            if boss_name in ['phreeoni']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['phreeoni'], "is_abyss": isAbyss})
            elif boss_name in ['mistress']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['mistress'], "is_abyss": isAbyss})
            elif boss_name in ['kraken']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['kraken'], "is_abyss": isAbyss})
            elif boss_name in ['eddga']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['eddga'], "is_abyss": isAbyss})
            elif boss_name in ['orc hero', 'hero']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['orchero'], "is_abyss": isAbyss})
            elif boss_name in ['maya']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['maya'], "is_abyss": isAbyss})
            elif boss_name in ['pharaoh']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['pharaoh'], "is_abyss": isAbyss})
            elif boss_name in ['orc lord', 'lord']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['orclord'], "is_abyss": isAbyss})
            # MINI
            elif boss_name in ['eclipse']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['eclipse'], "is_abyss": isAbyss})
            elif boss_name in ['mastering']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['mastering'], "is_abyss": isAbyss})
            elif boss_name in ['ghosting', 'ghost']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['ghosting'], "is_abyss": isAbyss})
            elif boss_name in ['toad']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['toad'], "is_abyss": isAbyss})
            elif boss_name in ['dragon fly', 'dragon']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['dragonfly'], "is_abyss": isAbyss})
            elif boss_name in ['king dramoh', 'king', 'dramoh']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['kingdramoh'], "is_abyss": isAbyss})
            elif boss_name in ['angeling', 'angel']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['angeling'], "is_abyss": isAbyss})
            elif boss_name in ['deviling', 'devil']:
                webhook_repo.send_message_webhook(
                    'refreshing', {"boss_data": config.BOSS_DATAS['deviling'], "is_abyss": isAbyss})


def blackwhite_image_processing(frame):
    # Get local maximum:
    kernelSize = 5
    maxKernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (kernelSize, kernelSize)
    )
    localMax = cv2.morphologyEx(
        frame, cv2.MORPH_CLOSE, maxKernel, None, None, 1, cv2.BORDER_REFLECT101
    )
    # Perform gain division
    gainDivision = np.where(
        localMax == 0, 0, (frame/localMax)
    )
    # Clip the values to [0,255]
    gainDivision = np.clip((255 * gainDivision), 0, 255)
    # Convert the mat type from float to uint8:
    gainDivision = gainDivision.astype("uint8")
    # Convert RGB to grayscale:
    grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Get binary image via Otsu:
    _, frame = cv2.threshold(
        grayscaleImage, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Flood fill (white + black):
    cv2.floodFill(frame, mask=None, seedPoint=(
        int(0), int(0)), newVal=(255))
    # Invert image so target blobs are colored in white:
    frame = 255 - frame
    return frame
