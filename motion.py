# -*- coding: UTF-8 -*-
import board

pin_map = board.pin_map

# Define the movements and their pin configuration
moves = {
    "Stop Moving": {
        "key": "X",
        "pins": {
            board.pins["AIN1"][pin_map]: "LOW",
            board.pins["AIN2"][pin_map]: "LOW",
            board.pins["BIN1"][pin_map]: "LOW",
            board.pins["BIN2"][pin_map]: "LOW"
        }
    },
    "Move Forward": {
        "key": "W",
        "pins": {
            board.pins["AIN1"][pin_map]: "HIGH",
            board.pins["AIN2"][pin_map]: "LOW",
            board.pins["BIN1"][pin_map]: "LOW",
            board.pins["BIN2"][pin_map]: "HIGH"
        }
    },
    "Move Backward": {
        "key": "S",
        "pins": {
            board.pins["AIN1"][pin_map]: "LOW",
            board.pins["AIN2"][pin_map]: "HIGH",
            board.pins["BIN1"][pin_map]: "HIGH",
            board.pins["BIN2"][pin_map]: "LOW"
        }
    },
    "Turn Left": {
        "key": "A",
        "pins": {
            board.pins["AIN1"][pin_map]: "LOW",
            board.pins["AIN2"][pin_map]: "LOW",
            board.pins["BIN1"][pin_map]: "LOW",
            board.pins["BIN2"][pin_map]: "HIGH"
        }
    },
    "Turn Right": {
        "key": "D",
        "pins": {
            board.pins["AIN1"][pin_map]: "HIGH",
            board.pins["AIN2"][pin_map]: "LOW",
            board.pins["BIN1"][pin_map]: "LOW",
            board.pins["BIN2"][pin_map]: "LOW"
        }
    },
    "Spin Left": {
        "key": "Q",
        "pins": {
            board.pins["AIN1"][pin_map]: "LOW",
            board.pins["AIN2"][pin_map]: "HIGH",
            board.pins["BIN1"][pin_map]: "LOW",
            board.pins["BIN2"][pin_map]: "HIGH"
        }
    },
    "Spin Right": {
        "key": "E",
        "pins": {
            board.pins["AIN1"][pin_map]: "HIGH",
            board.pins["AIN2"][pin_map]: "LOW",
            board.pins["BIN1"][pin_map]: "HIGH",
            board.pins["BIN2"][pin_map]: "LOW"
        }
    }
}


def show_controls():
    """
    Show the key and label for each possible move.

    :return: The function does not return anything.
    """
    key_list = moves.keys()
    for entry in key_list:
        key = get_key(entry)
        print(key, entry, sep=": ")


def get_key(direction):
    """
    Return the key mapped to the desired direction, as defined in the moves dictionary.

    :param direction: The desired direction in string form.
    :return: The button mapped to the direction in string form.
    """
    key = moves[direction]["key"]
    return key


def set_movement(direction):
    """
    Set the desired output to pins AIN1, AIN2, BIN1. BIN2.

    :param direction: The desired direction in string form.
    :return: The function does not return anything.
    """
    for k, v in moves[direction]["pins"].items():
        board.set_output(k, v)


def select_movement():
    action = input("Enter choice: ").upper()
    # TODO: add support for action to be set otherwise

    buttons = []
    for entry in moves.keys():
        key = get_key(entry)
        buttons.append(key)

    while action not in buttons:
        print("Invalid choice.")
        action = input("Enter new choice: ").upper()

    for button in buttons:
        for entry in moves.keys():
            if action == moves[entry]["key"]:
                set_movement(entry)
