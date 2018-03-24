# -*- coding: UTF-8 -*-
import time

import pins


def get_reflection():
    while True:
        status = pins.read_input(pins.pins["RSIN"]["pin"])
        if status == 1:
            print("Reflective")
        else:
            print("Non-Reflective")
        time.sleep(0.1)
        # TODO: Replace text output with a simple return value
        # return status


def get_distance(sensor):
    ping_time = 0
    echo_time = 0
    if sensor == 0:
        pins.set_output(pins.pins["ESO1"]["pin"], "low")
        pins.set_output(pins.pins["ESO1"]["pin"], "high")
        ping_time = time.time()
        time.sleep(0.00001)
        pins.set_output(pins.pins["RSO1"]["pin"], "low")

        while pins.read_input(pins.pins["ESIN"]["pin"]) == 0:
            ping_time = time.time()
        while pins.read_input(pins.pins["ESIN"]["pin"]) == 1:
            echo_time = time.time()

        if (echo_time is not None) and (ping_time is not None):
            elapsed_time = echo_time - ping_time
            distance = elapsed_time * 17000
        else:
            distance = 0
        print("Ping: {ping_time} - Echo: {echo_time}")
        return distance


while True:
    distance = get_distance(0)
    print(str(distance) + "\n")
    time.sleep(0.25)
