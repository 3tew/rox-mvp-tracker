# -*- coding: utf-8 -*-
import os
import sys
import ctypes
from threading import Thread
from pynput import keyboard
import mss

import config
from repositories import func_repo
from repositories import detector_repo

config.PID = os.getpid()
config.SCREENSHOT = mss.mss()

ctypes.windll.kernel32.SetConsoleTitleW(
    config.TITLE + ' ' + str(config.VERSION))
# Clear console
os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print("Press 'Q' button to exit program.\n")


def main_function():
    # Processing
    detector_repo.running_step()


if __name__ == "__main__":
    # Set title
    ctypes.windll.kernel32.SetConsoleTitleW(config.TITLE)
    print(config.TITLE)
    print("Made by Thanapat Maliphan. (fb.com/thanatos1995)\n")

    # Send started message
    detector_repo.send_message_webhook('', 'bot_start')

    func_repo.select_emulator()

    # Start thread
    thread1 = Thread(target=main_function)
    thread2 = keyboard.Listener(on_press=func_repo.on_press)
    # Start thread
    thread1.start()
    thread2.start()  # start to listen on a separate thread
    # Thread terminate
    thread1.join()
    thread2.join()  # remove if main thread is polling self.keys

    # Send started message
    detector_repo.send_message_webhook('', 'bot_stop')
    # Exit program
    sys.exit(0)
