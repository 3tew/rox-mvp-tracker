# -*- coding: utf-8 -*-
import os
import pyautogui
from pynput import keyboard
import mss
import logging

import config
from repositories import func_repo
from repositories import detector_repo


logging.basicConfig(filename='error.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

config.PID = os.getpid()
config.SCREENSHOT = mss.mss()

# disable this fail-safe (for multiple display monitor)
pyautogui.FAILSAFE = False

# Clear console
os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print(config.TITLE)
print("Develop by Thanapat Maliphan. (fb.com/thanatos1995)\n")
print("Press 'Q' button to exit program.")
print("Press 'P' button to toggle pause.\n")


def main_function():
    # Processing
    detector_repo.running()


with keyboard.Listener(on_press=func_repo.on_press) as listener:
    try:
        # Load webhooks
        func_repo.get_webhook_urls()
        # Find an android emulator
        func_repo.select_emulator()
        # Process
        main_function()
        # Terminate listener
        listener.join()
    except Exception as err:
        logger.error(err)
