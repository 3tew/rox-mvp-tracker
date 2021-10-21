# -*- coding: utf-8 -*-
import config

import cv2
import numpy as np


def show():
    # Debugging
    if config.IS_DEVELOPMENT:
        # Resize
        scale_percent = 60  # percent of original size
        width = int(
            config.FRAME_EMULATOR_RGB.shape[1] * scale_percent / 100)
        height = int(
            config.FRAME_EMULATOR_RGB.shape[0] * scale_percent / 100)
        resized = cv2.resize(config.FRAME_EMULATOR_RGB, (width, height))

        # Rendering
        cv2.imshow('RO:X - MVP Tracker v%s - Debugging' % config.VERSION,
                   np.hstack([resized]))


def render_notice_bounding():
    config.NOTICE_BOUNDING_BOX["x1"] = int((30 * config.EMULATOR_WIDTH) / 100)
    config.NOTICE_BOUNDING_BOX["y1"] = int(
        (23.75 * config.EMULATOR_HEIGHT) / 100)
    config.NOTICE_BOUNDING_BOX["x2"] = int((70 * config.EMULATOR_WIDTH) / 100)
    config.NOTICE_BOUNDING_BOX["y2"] = int((27 * config.EMULATOR_HEIGHT) / 100)

    if config.IS_DEVELOPMENT:
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.NOTICE_BOUNDING_BOX["x1"],
                config.NOTICE_BOUNDING_BOX["y1"]
            ),  # Point 1
            (
                config.NOTICE_BOUNDING_BOX["x2"],
                config.NOTICE_BOUNDING_BOX["y2"]
            ),  # Point 2
            (0, 0, 255), 1  # Color, Thickness
        )


def render_mvp_tab_bounding():
    # MVP
    config.MVP_BOUNDING_BOX["x1"] = int((13 * config.EMULATOR_WIDTH) / 100)
    config.MVP_BOUNDING_BOX["y1"] = int((19 * config.EMULATOR_HEIGHT) / 100)
    config.MVP_BOUNDING_BOX["x2"] = int((16 * config.EMULATOR_WIDTH) / 100)
    config.MVP_BOUNDING_BOX["y2"] = int((24 * config.EMULATOR_HEIGHT) / 100)
    config.MVP_BOUNDING_BOX_CENTER_X = int(
        config.MVP_BOUNDING_BOX["x1"] +
        ((config.MVP_BOUNDING_BOX["x2"] - config.MVP_BOUNDING_BOX["x1"]) / 2)
    )
    config.MVP_BOUNDING_BOX_CENTER_Y = int(config.MVP_BOUNDING_BOX["y1"] + (
        (config.MVP_BOUNDING_BOX["y2"] - config.MVP_BOUNDING_BOX["y1"]) / 2))
    # MINI
    config.MINI_BOUNDING_BOX["x1"] = int((23 * config.EMULATOR_WIDTH) / 100)
    config.MINI_BOUNDING_BOX["y1"] = int((19 * config.EMULATOR_HEIGHT) / 100)
    config.MINI_BOUNDING_BOX["x2"] = int((26 * config.EMULATOR_WIDTH) / 100)
    config.MINI_BOUNDING_BOX["y2"] = int((24 * config.EMULATOR_HEIGHT) / 100)
    config.MINI_BOUNDING_BOX_CENTER_X = int(config.MINI_BOUNDING_BOX["x1"] + (
        (config.MINI_BOUNDING_BOX["x2"] - config.MINI_BOUNDING_BOX["x1"]) / 2))
    config.MINI_BOUNDING_BOX_CENTER_Y = int(config.MINI_BOUNDING_BOX["y1"] + (
        (config.MINI_BOUNDING_BOX["y2"] - config.MINI_BOUNDING_BOX["y1"]) / 2))

    if config.IS_DEVELOPMENT:
        # MVP Tab
        cv2.rectangle(  # Bounding
            config.FRAME_EMULATOR_RGB,
            (
                config.MVP_BOUNDING_BOX["x1"],
                config.MVP_BOUNDING_BOX["y1"]
            ),  # Point 1
            (
                config.MVP_BOUNDING_BOX["x2"],
                config.MVP_BOUNDING_BOX["y2"]
            ),  # Point 2
            (0, 0, 255), 1  # Color, Thickness
        )
        cv2.rectangle(  # Center point
            config.FRAME_EMULATOR_RGB,
            (
                config.MVP_BOUNDING_BOX_CENTER_X,
                config.MVP_BOUNDING_BOX_CENTER_Y
            ),  # Point 1
            (
                config.MVP_BOUNDING_BOX_CENTER_X,
                config.MVP_BOUNDING_BOX_CENTER_Y
            ),  # Point 2
            (0, 0, 255), 5  # Color, Thickness
        )
        # MINI Tab
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.MINI_BOUNDING_BOX["x1"],
                config.MINI_BOUNDING_BOX["y1"]
            ),  # Point 1
            (
                config.MINI_BOUNDING_BOX["x2"],
                config.MINI_BOUNDING_BOX["y2"]
            ),  # Point 2
            (0, 0, 255), 1  # Color, Thickness
        )
        cv2.rectangle(  # Center point
            config.FRAME_EMULATOR_RGB,
            (
                config.MINI_BOUNDING_BOX_CENTER_X,
                config.MINI_BOUNDING_BOX_CENTER_Y
            ),  # Point 1
            (
                config.MINI_BOUNDING_BOX_CENTER_X,
                config.MINI_BOUNDING_BOX_CENTER_Y
            ),  # Point 2
            (0, 0, 255), 5  # Color, Thickness
        )


def render_boss_status_bounding():
    config.BOSS_STATUS_BOUNDING_BOX_0["x1"] = int(
        (38 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_0["y1"] = int(
        (16 * config.EMULATOR_HEIGHT) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_0["x2"] = int(
        (46 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_0["y2"] = int(
        (16.5 * config.EMULATOR_HEIGHT) / 100)

    config.BOSS_STATUS_BOUNDING_BOX_1["x1"] = int(
        (38 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_1["y1"] = int(
        (30 * config.EMULATOR_HEIGHT) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_1["x2"] = int(
        (46 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_1["y2"] = int(
        (37.5 * config.EMULATOR_HEIGHT) / 100)

    config.BOSS_STATUS_BOUNDING_BOX_2["x1"] = int(
        (38 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_2["y1"] = int(
        (46 * config.EMULATOR_HEIGHT) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_2["x2"] = int(
        (46 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_2["y2"] = int(
        (53.5 * config.EMULATOR_HEIGHT) / 100)

    config.BOSS_STATUS_BOUNDING_BOX_3["x1"] = int(
        (38 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_3["y1"] = int(
        (62 * config.EMULATOR_HEIGHT) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_3["x2"] = int(
        (46 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_3["y2"] = int(
        (69.5 * config.EMULATOR_HEIGHT) / 100)

    config.BOSS_STATUS_BOUNDING_BOX_4["x1"] = int(
        (38 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_4["y1"] = int(
        (78 * config.EMULATOR_HEIGHT) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_4["x2"] = int(
        (46 * config.EMULATOR_WIDTH) / 100)
    config.BOSS_STATUS_BOUNDING_BOX_4["y2"] = int(
        (85.5 * config.EMULATOR_HEIGHT) / 100)

    # Setup mouse drag position
    config.MOUSE_DRAG_CENTER_X_1 = int(config.BOSS_STATUS_BOUNDING_BOX_4["x1"] + (
        (config.BOSS_STATUS_BOUNDING_BOX_4["x2"] - config.BOSS_STATUS_BOUNDING_BOX_4["x1"]) / 2))
    config.MOUSE_DRAG_CENTER_Y_1 = int(config.BOSS_STATUS_BOUNDING_BOX_4["y1"] + (
        (config.BOSS_STATUS_BOUNDING_BOX_4["y2"] - config.BOSS_STATUS_BOUNDING_BOX_4["y1"]) / 2))

    config.MOUSE_DRAG_CENTER_X_2 = int(config.BOSS_STATUS_BOUNDING_BOX_0["x1"] + (
        (config.BOSS_STATUS_BOUNDING_BOX_0["x2"] - config.BOSS_STATUS_BOUNDING_BOX_0["x1"]) / 2))
    config.MOUSE_DRAG_CENTER_Y_2 = int(config.BOSS_STATUS_BOUNDING_BOX_0["y1"] + (
        (config.BOSS_STATUS_BOUNDING_BOX_0["y2"] - config.BOSS_STATUS_BOUNDING_BOX_0["y1"]) / 2))

    if config.IS_DEVELOPMENT:
        # Box 1
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.BOSS_STATUS_BOUNDING_BOX_1["x1"],
                config.BOSS_STATUS_BOUNDING_BOX_1["y1"]
            ),  # Point 1
            (
                config.BOSS_STATUS_BOUNDING_BOX_1["x2"],
                config.BOSS_STATUS_BOUNDING_BOX_1["y2"]
            ),  # Point 2
            (0, 0, 255), 1  # Color, Thickness
        )
        # Box 2
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.BOSS_STATUS_BOUNDING_BOX_2["x1"],
                config.BOSS_STATUS_BOUNDING_BOX_2["y1"]
            ),  # Point 1
            (
                config.BOSS_STATUS_BOUNDING_BOX_2["x2"],
                config.BOSS_STATUS_BOUNDING_BOX_2["y2"]
            ),  # Point 2
            (0, 0, 255), 1  # Color, Thickness
        )
        # Box 3
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.BOSS_STATUS_BOUNDING_BOX_3["x1"],
                config.BOSS_STATUS_BOUNDING_BOX_3["y1"]
            ),  # Point 1
            (
                config.BOSS_STATUS_BOUNDING_BOX_3["x2"],
                config.BOSS_STATUS_BOUNDING_BOX_3["y2"]
            ),  # Point 2
            (0, 0, 255), 1  # Color, Thickness
        )
        # Box 4
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.BOSS_STATUS_BOUNDING_BOX_4["x1"],
                config.BOSS_STATUS_BOUNDING_BOX_4["y1"]
            ),  # Point 1
            (
                config.BOSS_STATUS_BOUNDING_BOX_4["x2"],
                config.BOSS_STATUS_BOUNDING_BOX_4["y2"]
            ),  # Point 2
            (0, 0, 255), 1  # Color, Thickness
        )
        # Mouse drag start postion
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.MOUSE_DRAG_CENTER_X_1,
                config.MOUSE_DRAG_CENTER_Y_1
            ),  # Point 1
            (
                config.MOUSE_DRAG_CENTER_X_1,
                config.MOUSE_DRAG_CENTER_Y_1
            ),  # Point 2
            (0, 255, 0), 5  # Color, Thickness
        )
        # Mouse drag stop postion
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.MOUSE_DRAG_CENTER_X_2,
                config.MOUSE_DRAG_CENTER_Y_2
            ),  # Point 1
            (
                config.MOUSE_DRAG_CENTER_X_2,
                config.MOUSE_DRAG_CENTER_Y_2
            ),  # Point 2
            (0, 255, 0), 5  # Color, Thickness
        )


def render_disconnect_dialog_bounding():
    config.DISCONNECT_DIALOG_BOUNDING_BOX["x1"] = int(
        (52 * config.EMULATOR_WIDTH) / 100)
    config.DISCONNECT_DIALOG_BOUNDING_BOX["y1"] = int(
        (53 * config.EMULATOR_HEIGHT) / 100)
    config.DISCONNECT_DIALOG_BOUNDING_BOX["x2"] = int(
        (55 * config.EMULATOR_WIDTH) / 100)
    config.DISCONNECT_DIALOG_BOUNDING_BOX["y2"] = int(
        (56 * config.EMULATOR_HEIGHT) / 100)

    if config.IS_DEVELOPMENT:
        cv2.rectangle(
            config.FRAME_EMULATOR_RGB,
            (
                config.DISCONNECT_DIALOG_BOUNDING_BOX['x1'],
                config.DISCONNECT_DIALOG_BOUNDING_BOX['y1']
            ),  # Point 1
            (
                config.DISCONNECT_DIALOG_BOUNDING_BOX['x2'],
                config.DISCONNECT_DIALOG_BOUNDING_BOX['y2']
            ),  # Point 2
            (0, 255, 255), 1  # Color, Thickness
        )
