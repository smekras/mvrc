# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PWMA = 18
AIN1 = 17
AIN2 = 4
PWMB = 10
BIN1 = 27
BIN2 = 22

pins = [PWMA, AIN1, AIN2, PWMB, BIN1, BIN2]

moves = {
    "Stop Moving": {
        "button": "X",
        "pins": {
            AIN1: GPIO.LOW,
            AIN2: GPIO.LOW,
            BIN1: GPIO.LOW,
            BIN2: GPIO.LOW
        }
    },
    "Move Forward": {
        "button": "W",
        "pins": {
            AIN1: GPIO.HIGH,
            AIN2: GPIO.LOW,
            BIN1: GPIO.LOW,
            BIN2: GPIO.HIGH
        }
    },
    "Move Backward": {
        "button": "S",
        "pins": {
            AIN1: GPIO.LOW,
            AIN2: GPIO.HIGH,
            BIN1: GPIO.HIGH,
            BIN2: GPIO.LOW
        }
    },
    "Turn Left": {
        "button": "A",
        "pins": {
            AIN1: GPIO.LOW,
            AIN2: GPIO.LOW,
            BIN1: GPIO.LOW,
            BIN2: GPIO.HIGH
        }
    },
    "Turn Right": {
        "button": "D",
        "pins": {
            AIN1: GPIO.HIGH,
            AIN2: GPIO.LOW,
            BIN1: GPIO.LOW,
            BIN2: GPIO.LOW
        }
    },
    "Spin Left": {
        "button": "Q",
        "pins": {
            AIN1: GPIO.LOW,
            AIN2: GPIO.HIGH,
            BIN1: GPIO.LOW,
            BIN2: GPIO.HIGH
        }
    },
    "Spin Right": {
        "button": "E",
        "pins": {
            AIN1: GPIO.HIGH,
            AIN2: GPIO.LOW,
            BIN1: GPIO.HIGH,
            BIN2: GPIO.LOW
        }
    }
}


def pin_handler(action):
    for pin in pins:
        if action == "prime":
            GPIO.setup(pin, GPIO.OUT)
        else:
            GPIO.setup(pin, GPIO.IN)


def movement(direction):
    for k, v in moves[direction]["pins"].items():
        GPIO.output(k, v)


def get_button(direction):
    button = moves[direction]["button"]
    return button
