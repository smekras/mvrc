# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO

mode = None

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


def select_mode():
    """
    Set mapping mode and disable GPIO warnings.

    :return: The function does not return anything.
    """
    global mode
    mode = input("Select mode (BCM|BOARD)").upper()
    setattr(GPIO, "setmode", mode)
    setattr(GPIO, "setwarnings", False)


def pin_handler(action):
    """
    Prime the pins for use by components,
    based on the state set in the pins dictionary.

    :param action: The desired action in string form.
    :return: The function does not return anything.
    """
    for pin in pins.keys():
        if action == "prime":
            state = "GPIO." + pins[pin]["state"]
        else:
            state = GPIO.IN

        setattr(GPIO, "setup", (pins[pin][mode], state))


def read_input(pin):
    """
    Read an input pin and return the value.

    :param pin: The number of the desired pin.
    :return: The function returns the input value.
    """
    return getattr(GPIO, "input", pin)


def set_output(pin, value):
    """
    Set the output value of a pin.

    :param pin: The number of the desired pin.
    :param value: The desired output value.
    :return: The function does not return anything.
    """
    output_value = "GPIO." + value
    setattr(GPIO, "output", (pin, output_value))
