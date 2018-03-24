# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = {
    "PWMA": {
        "pin": 18,
        "mode": "PWM"
    },
    "PWMB": {
        "pin": 13,
        "mode": "PWM"
    },
    "RSIN": {
        "pin": 23,
        "mode": "IN"
    },
    "ESIN": {
        "pin": 2,
        "mode": "IN"
    },
    "ESO1": {
        "pin": 3,
        "mode": "OUT"
    },
    "AIN1": {
        "pin": 17,
        "mode": "OUT"
    },
    "AIN2": {
        "pin": 4,
        "mode": "OUT"
    },
    "BIN1": {
        "pin": 27,
        "mode": "OUT"
    },
    "BIN2": {
        "pin": 22,
        "mode": "OUT"
    }
}

moves = {
    "Stop Moving": {
        "button": "X",
        "pins": {
            pins["AIN1"]["pin"]: GPIO.LOW,
            pins["AIN2"]["pin"]: GPIO.LOW,
            pins["BIN1"]["pin"]: GPIO.LOW,
            pins["BIN2"]["pin"]: GPIO.LOW
        }
    },
    "Move Forward": {
        "button": "W",
        "pins": {
            pins["AIN1"]["pin"]: GPIO.HIGH,
            pins["AIN2"]["pin"]: GPIO.LOW,
            pins["BIN1"]["pin"]: GPIO.LOW,
            pins["BIN2"]["pin"]: GPIO.HIGH
        }
    },
    "Move Backward": {
        "button": "S",
        "pins": {
            pins["AIN1"]["pin"]: GPIO.LOW,
            pins["AIN2"]["pin"]: GPIO.HIGH,
            pins["BIN1"]["pin"]: GPIO.HIGH,
            pins["BIN2"]["pin"]: GPIO.LOW
        }
    },
    "Turn Left": {
        "button": "A",
        "pins": {
            pins["AIN1"]["pin"]: GPIO.LOW,
            pins["AIN2"]["pin"]: GPIO.LOW,
            pins["BIN1"]["pin"]: GPIO.LOW,
            pins["BIN2"]["pin"]: GPIO.HIGH
        }
    },
    "Turn Right": {
        "button": "D",
        "pins": {
            pins["AIN1"]["pin"]: GPIO.HIGH,
            pins["AIN2"]["pin"]: GPIO.LOW,
            pins["BIN1"]["pin"]: GPIO.LOW,
            pins["BIN2"]["pin"]: GPIO.LOW
        }
    },
    "Spin Left": {
        "button": "Q",
        "pins": {
            pins["AIN1"]["pin"]: GPIO.LOW,
            pins["AIN2"]["pin"]: GPIO.HIGH,
            pins["BIN1"]["pin"]: GPIO.LOW,
            pins["BIN2"]["pin"]: GPIO.HIGH
        }
    },
    "Spin Right": {
        "button": "E",
        "pins": {
            pins["AIN1"]["pin"]: GPIO.HIGH,
            pins["AIN2"]["pin"]: GPIO.LOW,
            pins["BIN1"]["pin"]: GPIO.HIGH,
            pins["BIN2"]["pin"]: GPIO.LOW
        }
    }
}


def pin_handler(action):
    for pin in pins:
        if action == "prime":
            GPIO.setup(pin, GPIO.OUT)
        else:
            GPIO.setup(pin, GPIO.IN)


def read_input(pin):
    status = GPIO.input(pin)
    return status


def set_output(pin, value):
    output = GPIO.LOW
    if value is "high":
        output = GPIO.HIGH
    GPIO.output(pin, output)


def movement(direction):
    for k, v in moves[direction]["pins"].items():
        set_output(k, v)


def get_button(direction):
    button = moves[direction]["button"]
    return button
