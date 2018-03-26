# -*- coding: UTF-8 -*-
import RPi.GPIO as IO

import utils

# Load configuration file
config = utils.json_to_dict('config.json')
pin_map = config["map"]
pin_control = config["control"]

# Define mapping, states, and values, for pins
controls = {"I": "Prime Pins", "O": "Reset Pins"}
maps = {"BCM": IO.BCM, "BOARD": IO.BOARD}
states = {"IN": IO.IN, "OUT": IO.OUT}
values = {"HIGH": IO.HIGH, "LOW": IO.LOW}

# Define the pins and their active state
pins = {
    "AIN1": {
        "BCM": 4,
        "BOARD": 7,
        "state": "OUT"
    },
    "AIN2": {
        "BCM": 17,
        "BOARD": 11,
        "state": "OUT"
    },
    "BIN1": {
        "BCM": 27,
        "BOARD": 13,
        "state": "OUT"
    },
    "BIN2": {
        "BCM": 22,
        "BOARD": 15,
        "state": "OUT"
    },
    "ESIN": {
        "BCM": 2,
        "BOARD": 3,
        "state": "IN"
    },
    "ESO1": {
        "BCM": 3,
        "BOARD": 5,
        "state": "OUT"
    },
    "PWMA": {
        "BCM": 18,
        "BOARD": 12,
        "state": "OUT"
    },
    "PWMB": {
        "BCM": 13,
        "BOARD": 33,
        "state": "OUT"
    },
    "RSIN": {
        "BCM": 23,
        "BOARD": 16,
        "state": "IN"
    }
}


def init_board():
    IO.setmode(maps[pin_map])
    IO.setwarnings(False)


def map_pins():
    config["map"] = input("Enter pin mapping (BCM|BOARD): ").upper
    utils.dict_to_json(config)


def control_pins():
    utils.print_dict(controls)
    choice = input("Enter choice: ").upper()
    config["control"] = controls[choice]
    set_pins(config["control"])


def set_pins(action):
    for entry in pins.keys():
        pin = pins[entry]
        if action == "prime":
            state = states[pin["state"]]
        else:
            state = states["IN"]

        if pin["state"] is "OUT":
            IO.setup(pin[pin_map], state, initial=0)
        else:
            IO.setup(pin[pin_map], state)


def get_input(pin):
    return IO.input(pin)


def set_output(pin, value):
    output_value = values[value]
    IO.output(pin, output_value)
