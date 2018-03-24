# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO

# Define the pins and their active mode
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


def select_mode(mode):
    """
    Set mapping mode and disable GPIO warnings.

    :param mode: The mapping mode for the raspberry pi.
    :return: The function does not return anything.
    """
    mode_choice = "GPIO." + mode
    GPIO.setmode(mode_choice.strip('\"'))
    GPIO.setwarnings(False)


def pin_handler(action, mode):
    """
    Prime the pins for use by components,
    based on the state set in the pins dictionary.

    :param action: The desired action in string form.
    :param mode: The mapping mode for the raspberry pi.
    :return: The function does not return anything.
    """
    for pin in pins.keys():
        if action == "prime":
            state = "GPIO." + pins[pin]["state"]
            GPIO.setup(pins[pin][mode], state.strip('\"'))
        else:
            GPIO.setup(pins[pin][mode], GPIO.IN)


def read_input(pin):
    """
    Read an input pin and return the value.

    :param pin: The number of the desired pin.
    :return: The function returns the input value.
    """
    status = GPIO.input(pin)
    return status


def set_output(pin, value):
    """
    Set the output value of a pin.

    :param pin: The number of the desired pin.
    :param value: The desired output value.
    :return: The function does not return anything.
    """
    output_value = "GPIO." + value
    GPIO.output(pin, output_value.strip('\"'))
