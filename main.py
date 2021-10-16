# -*- coding: utf-8 -*-
import os
import sys
import pyautogui
from threading import Thread
from pynput import keyboard
import mss

import config
from repositories import func_repo
from repositories import detector_repo

config.PID = os.getpid()
config.SCREENSHOT = mss.mss()

# disable this fail-safe (for multiple display monitor)
pyautogui.FAILSAFE = False

# Clear console
os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print(config.TITLE)
print("Develop by Thanapat Maliphan. (fb.com/thanatos1995)\n")
print("Press 'Q' button to exit program.\n")


def main_function():
    # Processing
    detector_repo.running()
    # Finish program
    sys.exit(0)


if __name__ == "__main__":
    # Load webhooks
    func_repo.get_webhook_urls()
    # Find an android emulator
    func_repo.select_emulator()
    # Initialize threads
    thread1 = Thread(target=main_function)
    thread2 = keyboard.Listener(on_press=func_repo.on_press)
    # Start threads
    thread1.start()
    thread2.start()
    # Threads terminated
    thread1.join()
    thread2.join()
    # Send shutting down message
    detector_repo.send_message_webhook('', 'bot_stop')
    # Exit program
    sys.exit(0)
