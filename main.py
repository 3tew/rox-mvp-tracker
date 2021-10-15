# -*- coding: utf-8 -*-
import os
import sys
import ctypes
from threading import Thread
import time
from pynput import keyboard
import numpy as np
import cv2
import mss
from win32api import GetSystemMetrics

import config
from repositories import func_repo
from repositories import render_repo
from repositories import detector_repo

config.PID = os.getpid()
config.SCREENSHOT = mss.mss()

ctypes.windll.kernel32.SetConsoleTitleW(
    config.TITLE + ' ' + str(config.VERSION))
# Clear console
os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print("Press 'Q' button to exit program.\n")


def main_function():
    while config.IS_RUNNING:
        # ดักปุ่มกด
        key = cv2.waitKey(25)
        # Press "Q" button to exit program
        if key & 0xFF == ord('q'):
            config.IS_RUNNING = False
            cv2.destroyAllWindows()
            break

        # Set current time
        config.CURRENT_TIME = time.time()

        # Crop
        func_repo.get_emulator_area()
        
        render_repo.render_notice_bounding()
        render_repo.render_mvp_tab_bounding()
        render_repo.render_boss_status_bounding()

        # แปลงสีภาพ
        config.FRAME_EMULATOR_RGB = cv2.cvtColor(
            np.array(config.FRAME_EMULATOR), cv2.COLOR_BGR2RGB)
        config.FRAME_EMULATOR_HSV = cv2.cvtColor(
            config.FRAME_EMULATOR_RGB, cv2.COLOR_BGR2HSV)

        # Processing
        detector_repo.running_step()

        render_repo.show(frame=config.FRAME_EMULATOR_RGB)


if __name__ == "__main__":
    # Set title
    ctypes.windll.kernel32.SetConsoleTitleW(config.TITLE)
    print(config.TITLE)
    print("Made by Thanapat Maliphan. (fb.com/thanatos1995)\n")
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

    # Exit program
    sys.exit(0)
