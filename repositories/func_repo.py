import config

import sys
import pyautogui
import pygetwindow
import re
import cv2
import time
import mss
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image

from repositories import webhook_repo

root = Tk()
root.withdraw()


def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['q', 'p']:  # keys of interest
        if k == 'p':
            config.IS_HOLD ^= True
            print("[SYSTEM]: Paused!") if config.IS_HOLD else print(
                "[SYSTEM]: Unpaused!")
        elif k == 'q':
            print("[SYSTEM]: Shutting down...")
            # Break while loop
            config.IS_RUNNING = False
            # Thread terminate
            sys.exit()


def mouse_click_mvp_tab():
    x = (config.EMULATOR_X + config.MVP_BOUNDING_BOX_CENTER_X)
    y = (config.EMULATOR_Y + config.MVP_BOUNDING_BOX_CENTER_Y)
    pyautogui.click(x=x, y=y)
    time.sleep(0.05)  # Delay 50 milliseconds


def mouse_click_mini_tab():
    x = (config.EMULATOR_X + config.MINI_BOUNDING_BOX_CENTER_X)
    y = (config.EMULATOR_Y + config.MINI_BOUNDING_BOX_CENTER_Y)
    pyautogui.click(x=x, y=y)
    time.sleep(0.05)  # Delay 50 milliseconds


def mouse_draging():
    x1 = (config.EMULATOR_X + config.MOUSE_DRAG_CENTER_X_1)
    y1 = (config.EMULATOR_Y + config.MOUSE_DRAG_CENTER_Y_1)
    x2 = (config.EMULATOR_X + config.MOUSE_DRAG_CENTER_X_2)
    y2 = (config.EMULATOR_Y + config.MOUSE_DRAG_CENTER_Y_2) - 80  # Calibrating
    pyautogui.moveTo(x=x1, y=y1)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=x2, y=y2, button='left',
                     duration=0.3, mouseDownUp=False)
    pyautogui.dragTo(x=x2, y=y2 + 5, button='left',  # Calibrating
                     duration=0.125, mouseDownUp=False)
    # time.sleep(0.25)  # Delay 250 milliseconds
    pyautogui.mouseUp(button='left')


def alert(title, message, kind='info'):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


def find_emulator(emulator_name):
    # Get titles of all specific window
    titles = pygetwindow.getAllTitles()

    # to get string with substring
    res = [x for x in titles if re.search(emulator_name, x)]
    if len(res) == 0:
        return False
    else:
        return True


def select_emulator():
    print("[SYSTEM]: Bot are supported on " +
          ' ,'.join(map(str, config.EMULATOR_NAMES)) + " only.")
    for emulator_name in config.EMULATOR_NAMES:
        print("[SYSTEM]: Finding " + emulator_name + ' emulator ...')
        if find_emulator(emulator_name):
            print("[SYSTEM]: " + emulator_name + ' detected!')
            config.EMULATOR_SELECTED = emulator_name
            return
    print("[ERROR]: Emulator not found.")
    alert('Error', 'Emulator not found', kind='error')
    sys.exit()


def get_emulator_screenshot(sct):
    try:
        window = pygetwindow.getWindowsWithTitle(config.EMULATOR_SELECTED)[0]
    except IndexError:
        # Send error notification
        webhook_repo.send_message_webhook(
            'error', {"reason": "Emulator terminated"})
        print('[ERROR]: Cant get emulator bounding box!')
        config.IS_RUNNING = False
        # Stop process
        sys.exit()

    config.EMULATOR_X = window.left
    config.EMULATOR_Y = window.top
    config.EMULATOR_WIDTH = window.width
    config.EMULATOR_HEIGHT = window.height

    try:
        sct.get_pixels(
            {'top': config.EMULATOR_Y, 'left': config.EMULATOR_X, 'width': config.EMULATOR_WIDTH, 'height': config.EMULATOR_HEIGHT})
    except mss.exception.ScreenshotError:
        print("[ERROR]: ScreenshotError exception.")

    try:
        # Set emulator frame
        config.FRAME_EMULATOR = Image.frombytes(
            'RGB', (sct.width, sct.height), sct.image)
    except ValueError:
        print("[ERROR]: ValueError, screenshot not found.")
        return None

    # Convert to RGB
    config.FRAME_EMULATOR_RGB = cv2.cvtColor(
        np.array(config.FRAME_EMULATOR), cv2.COLOR_BGR2RGB)


def get_bounding_frame(sct, bounding_area):
    BOUNDING_BOX = {
        'left': config.EMULATOR_X + bounding_area['x1'],
        'top': config.EMULATOR_Y + bounding_area['y1'],
        'width': (bounding_area['x2'] - bounding_area['x1']),
        'height': (bounding_area['y2'] - bounding_area['y1']),
    }

    # Get screenshot pixels
    try:
        sct.get_pixels(BOUNDING_BOX)
    except Exception as err:
        print("[ERROR]: Exception, " + err)

    # Set emulator frame
    try:
        frame = Image.frombytes(
            'RGB', (sct.width, sct.height), sct.image)
    except ValueError:
        print("[ERROR]: ValueError, screenshot not found.")
        return None

    rgb_frame = cv2.cvtColor(
        np.array(frame), cv2.COLOR_BGR2RGB)
    return rgb_frame


def get_webhook_urls():
    try:
        with open('webhooks.txt', 'r') as file:
            lines = file.readlines()
            config.DISCORD_WEBHOOK_URLS = [line.rstrip() for line in lines]
    except FileNotFoundError:
        print("[ERROR]: 'webhooks.txt' file not found.")
        alert('Error', "'webhooks.txt' file not found.", kind='error')
        sys.exit()
    print("[SYSTEM]: " + str(len(config.DISCORD_WEBHOOK_URLS)) + ' found webhooks.')
