import config

import sys
import pyautogui
import pygetwindow
import re
import cv2
import time
import numpy as np
from tkinter import *  
from tkinter import messagebox 
from PIL import Image

root = Tk()
root.withdraw()

def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['q']:  # keys of interest
        print("[SYSTEM]: Shutting down...")
        if k == 'q':
            # Break while loop
            config.IS_RUNNING = False
            # Thread terminate
            sys.exit(0)


def mouse_click_mvp_tab():
    x = (config.EMULATOR_X + config.MVP_BOUNDING_BOX_CENTER_X)
    y = (config.EMULATOR_Y + config.MVP_BOUNDING_BOX_CENTER_Y)
    pyautogui.click(x=x, y=y)
    time.sleep(0.4)  # Delay 400 milliseconds


def mouse_click_mini_tab():
    x = (config.EMULATOR_X + config.MINI_BOUNDING_BOX_CENTER_X)
    y = (config.EMULATOR_Y + config.MINI_BOUNDING_BOX_CENTER_Y)
    pyautogui.click(x=x, y=y)
    time.sleep(0.4)  # Delay 400 milliseconds


def mouse_draging():
    x1 = (config.EMULATOR_X + config.MOUSE_DRAG_CENTER_X_1)
    y1 = (config.EMULATOR_Y + config.MOUSE_DRAG_CENTER_Y_1)
    x2 = (config.EMULATOR_X + config.MOUSE_DRAG_CENTER_X_2)
    y2 = (config.EMULATOR_Y + config.MOUSE_DRAG_CENTER_Y_2) - 50  # Calibrating
    pyautogui.moveTo(x=x1, y=y1)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=x2, y=y2, button='left',
                     duration=0.35, mouseDownUp=False)
    time.sleep(0.25)  # Delay 250 milliseconds
    pyautogui.mouseUp(button='left')


def alert(title, message, kind='info'):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')
    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)


def find_emulator():
    # Get titles of all specific window
    titles = pygetwindow.getAllTitles()

    # to get string with substring
    res = [x for x in titles if re.search(config.EMULATOR_TEXT, x)]
    if len(res) == 0:
        alert('Error', 'Emulator not found', kind='error')
        sys.exit(1)


def select_emulator():
    config.EMULATOR_TEXT = 'LDPlayer'
    print("[SYSTEM]: Finding " + config.EMULATOR_TEXT + ' emulator...')
    find_emulator()
    print("[SYSTEM]: " + config.EMULATOR_TEXT + ' detected!')


def get_emulator_area():
    try:
        window = pygetwindow.getWindowsWithTitle(config.EMULATOR_TEXT)[0]
    except IndexError:
        alert(
            'Error', 'Can\'t get emulator bounding box', kind='error')
        sys.exit(1)
    config.EMULATOR_X = window.left
    config.EMULATOR_Y = window.top
    config.EMULATOR_WIDTH = window.width
    config.EMULATOR_HEIGHT = window.height
    config.SCREENSHOT.get_pixels(
        {'top': config.EMULATOR_Y, 'left': config.EMULATOR_X, 'width': config.EMULATOR_WIDTH, 'height': config.EMULATOR_HEIGHT})
    # Set emulator frame
    config.FRAME_EMULATOR = Image.frombytes(
        'RGB', (config.SCREENSHOT.width, config.SCREENSHOT.height), config.SCREENSHOT.image)


def get_bounding_frame(bounding_area):
    BOUNDING_BOX = {
        'left': config.EMULATOR_X + bounding_area['x1'],
        'top': config.EMULATOR_Y + bounding_area['y1'],
        'width': (bounding_area['x2'] - bounding_area['x1']),
        'height': (bounding_area['y2'] - bounding_area['y1']),
    }
    config.SCREENSHOT.get_pixels(BOUNDING_BOX)
    frame = Image.frombytes(
        'RGB', (config.SCREENSHOT.width, config.SCREENSHOT.height), config.SCREENSHOT.image)
    rgb_frame = cv2.cvtColor(
        np.array(frame), cv2.COLOR_BGR2RGB)
    return rgb_frame


def crop_boss_notice_frame(bounding_area):
    BOUNDING_BOX = {
        'left': config.EMULATOR_X + bounding_area['x1'],
        'top': config.EMULATOR_Y + bounding_area['y1'],
        'width': (bounding_area['x2'] - bounding_area['x1']),
        'height': (bounding_area['y2'] - bounding_area['y1']),
    }
    # Text image processing
    config.SCREENSHOT.get_pixels(BOUNDING_BOX)
    config.FRAME_NOTICE_TEXT = Image.frombytes(
        'RGB', (config.SCREENSHOT.width, config.SCREENSHOT.height), config.SCREENSHOT.image)
    config.FRAME_NOTICE_TEXT = cv2.cvtColor(
        np.array(config.FRAME_NOTICE_TEXT), cv2.COLOR_BGR2RGB)

    # Copy
    config.FRAME_NOTICE_TEXT_RECOG = config.FRAME_NOTICE_TEXT

    # Get local maximum:
    kernelSize = 5
    maxKernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (kernelSize, kernelSize)
    )
    localMax = cv2.morphologyEx(
        config.FRAME_NOTICE_TEXT_RECOG, cv2.MORPH_CLOSE, maxKernel, None, None, 1, cv2.BORDER_REFLECT101
    )
    # Perform gain division
    gainDivision = np.where(
        localMax == 0, 0, (config.FRAME_NOTICE_TEXT_RECOG/localMax)
    )
    # Clip the values to [0,255]
    gainDivision = np.clip((255 * gainDivision), 0, 255)
    # Convert the mat type from float to uint8:
    gainDivision = gainDivision.astype("uint8")
    # Convert RGB to grayscale:
    grayscaleImage = cv2.cvtColor(gainDivision, cv2.COLOR_BGR2GRAY)
    # Get binary image via Otsu:
    _, config.FRAME_NOTICE_TEXT_RECOG = cv2.threshold(
        grayscaleImage, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Flood fill (white + black):
    cv2.floodFill(config.FRAME_NOTICE_TEXT_RECOG, mask=None, seedPoint=(
        int(0), int(0)), newVal=(255))
    # Invert image so target blobs are colored in white:
    config.FRAME_NOTICE_TEXT_RECOG = 255 - config.FRAME_NOTICE_TEXT_RECOG
