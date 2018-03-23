# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PWMA = 18
AIN1 = 17
AIN2 = 4
BIN1 = 27
BIN2 = 22

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

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


def movement(direction):
    for k, v in moves[direction]["pins"].items():
        GPIO.output(k, v)
