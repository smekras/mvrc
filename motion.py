# -*- coding: UTF-8 -*-
import board

# Define the movements and their pin configuration
moves = {
    "Stop Moving": {
        "button": "X",
        "pins": {
            board.pins["AIN1"]["BCM"]: "LOW",
            board.pins["AIN2"]["BCM"]: "LOW",
            board.pins["BIN1"]["BCM"]: "LOW",
            board.pins["BIN2"]["BCM"]: "LOW"
        }
    },
    "Move Forward": {
        "button": "W",
        "pins": {
            board.pins["AIN1"]["BCM"]: "HIGH",
            board.pins["AIN2"]["BCM"]: "LOW",
            board.pins["BIN1"]["BCM"]: "LOW",
            board.pins["BIN2"]["BCM"]: "HIGH"
        }
    },
    "Move Backward": {
        "button": "S",
        "pins": {
            board.pins["AIN1"]["BCM"]: "LOW",
            board.pins["AIN2"]["BCM"]: "HIGH",
            board.pins["BIN1"]["BCM"]: "HIGH",
            board.pins["BIN2"]["BCM"]: "LOW"
        }
    },
    "Turn Left": {
        "button": "A",
        "pins": {
            board.pins["AIN1"]["BCM"]: "LOW",
            board.pins["AIN2"]["BCM"]: "LOW",
            board.pins["BIN1"]["BCM"]: "LOW",
            board.pins["BIN2"]["BCM"]: "HIGH"
        }
    },
    "Turn Right": {
        "button": "D",
        "pins": {
            board.pins["AIN1"]["BCM"]: "HIGH",
            board.pins["AIN2"]["BCM"]: "LOW",
            board.pins["BIN1"]["BCM"]: "LOW",
            board.pins["BIN2"]["BCM"]: "LOW"
        }
    },
    "Spin Left": {
        "button": "Q",
        "pins": {
            board.pins["AIN1"]["BCM"]: "LOW",
            board.pins["AIN2"]["BCM"]: "HIGH",
            board.pins["BIN1"]["BCM"]: "LOW",
            board.pins["BIN2"]["BCM"]: "HIGH"
        }
    },
    "Spin Right": {
        "button": "E",
        "pins": {
            board.pins["AIN1"]["BCM"]: "HIGH",
            board.pins["AIN2"]["BCM"]: "LOW",
            board.pins["BIN1"]["BCM"]: "HIGH",
            board.pins["BIN2"]["BCM"]: "LOW"
        }
    }
}


def movement(direction):
    """
    Set the desired output to pins AIN1, AIN2, BIN1. BIN2.

    :param direction: The desired direction in string form.
    :return: The function does not return anything.
    """
    for k, v in moves[direction]["pins"].items():
        value = "GPIO." + v
        board.set_output(k, value)


def get_button(direction):
    """
    Return the key mapped to the desired direction,
    as defined in the moves dictionary.

    :param direction: The desired direction in string form.
    :return: The button mapped to the direction in string form.
    """
    button = moves[direction]["button"]
    return button
