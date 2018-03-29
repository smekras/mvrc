# -*- coding: UTF-8 -*-
import time

import RPi.GPIO as IO

import utils

# Load configuration file
config = utils.json_to_dict('config.json')
pin_map = config["Settings"]["map"]
pin_control = config["Settings"]["control"]

# Define mapping, states, and current, for pins
controls = {"I": "Prime Pins", "O": "Reset Pins"}
maps = {"BCM": IO.BCM, "BOARD": IO.BOARD}
states = {"IN": IO.IN, "OUT": IO.OUT}
current = {"HIGH": IO.HIGH, "LOW": IO.LOW}

# Define the pins and their active state
pins = config["Pins"]


def init_board():
    IO.setmode(maps[pin_map])
    IO.setwarnings(False)


def map_pins():
    config["Settings"]["map"] = input("Enter pin mapping (BCM|BOARD): ").upper
    utils.dict_to_json(config, 'config.json')


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
    output_value = current[value]
    IO.output(pin, output_value)


def blink_pin(pin, duration):
    timer_start = time.time()
    while time.time() < timer_start + duration:
        for value in [IO.HIGH, IO.LOW]:
            IO.output(pin, value)
            time.sleep(0.1)
