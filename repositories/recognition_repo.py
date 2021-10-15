import config
from repositories import func_repo
from repositories import detector_repo

import re
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def refreshing_text_detector():
    # Text recognition process...
    text = pytesseract.image_to_string(
        config.FRAME_NOTICE_TEXT
    )
    text = text.strip()
    text = text.lower()
    print("[SYSTEM]: Text = '" + text + "'")  # Debugging

    if any(boss_name in text for boss_name in config.BOSS_NAMES):
        if (config.CURRENT_TIME - config.NOTICE_TIME) > 15:  # ระยะเวลาระหว่างประกาศ 15 วินาที
            # Checking Abyss type
            abyssText = ''
            if 'abyss' in text:
                abyssText = 'Abyss '
            # MVP
            if boss_name in ['phreeoni']:
                detector_repo.send_message_webhook(
                    abyssText + 'Phreeoni', 'refreshing')
            elif boss_name in ['mistress']:
                detector_repo.send_message_webhook(
                    abyssText + 'Mistress', 'refreshing')
            elif boss_name in ['kraken']:
                detector_repo.send_message_webhook(
                    abyssText + 'Kraken', 'refreshing')
            elif boss_name in ['eddga']:
                detector_repo.send_message_webhook(
                    abyssText + 'Eddga', 'refreshing')
            elif boss_name in ['orc hero', 'hero']:
                detector_repo.send_message_webhook(
                    abyssText + 'Orc Hero', 'refreshing')
            elif boss_name in ['maya']:
                detector_repo.send_message_webhook(
                    abyssText + 'Maya', 'refreshing')
            elif boss_name in ['pharaoh']:
                detector_repo.send_message_webhook(
                    abyssText + 'Pharaoh', 'refreshing')
            elif boss_name in ['orc lord', 'lord']:
                detector_repo.send_message_webhook(
                    abyssText + 'Orc Lord', 'refreshing')
            # MINI
            elif boss_name in ['eclipse']:
                detector_repo.send_message_webhook('Eclipse', 'refreshing')
            elif boss_name in ['mastering']:
                detector_repo.send_message_webhook('Mastering', 'refreshing')
            elif boss_name in ['ghosting']:
                detector_repo.send_message_webhook('Ghosting', 'refreshing')
            elif boss_name in ['toad']:
                detector_repo.send_message_webhook('Toad', 'refreshing')
            elif boss_name in ['dragon fly', 'dragon', 'fly']:
                detector_repo.send_message_webhook('Dragon Fly', 'refreshing')
            elif boss_name in ['king dramoh', 'king', 'dramoh']:
                detector_repo.send_message_webhook('King Dramoh', 'refreshing')
            elif boss_name in ['angeling']:
                detector_repo.send_message_webhook('Angeling', 'refreshing')
            elif boss_name in ['deviling']:
                detector_repo.send_message_webhook('Deviling', 'refreshing')
