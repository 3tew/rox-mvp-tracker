# -*- coding: utf-8 -*-
import os
import sys
import logging
import pyautogui
from pynput import keyboard

import config
from repositories import func_repo
from repositories import detector_repo
from repositories import webhook_repo

config.PID = os.getpid()

logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)

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
        print(err)
        config.IS_RUNNING = False
        webhook_repo.send_logging_webhook(err)
        webhook_repo.send_message_webhook('error', {"reason": "Bot crashed"})
        sys.exit(1)
