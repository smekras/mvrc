# -*- coding: UTF-8 -*-
import time

import board


def get_reflection():
    while True:
        status = board.read_input(board.pins["RSIN"]["pin"])
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
        board.set_output(board.pins["ESO1"]["pin"], "low")
        board.set_output(board.pins["ESO1"]["pin"], "high")
        ping_time = time.time()
        time.sleep(0.00001)
        board.set_output(board.pins["RSO1"]["pin"], "low")

        while board.read_input(board.pins["ESIN"]["pin"]) == 0:
            ping_time = time.time()
        while board.read_input(board.pins["ESIN"]["pin"]) == 1:
            echo_time = time.time()

        if (echo_time is not None) and (ping_time is not None):
            elapsed_time = echo_time - ping_time
            distance = elapsed_time * 17000
        else:
            distance = 0
        print("Ping: {ping_time} - Echo: {echo_time}")
        return distance


while True:
    stretch = get_distance(0)
    print(str(stretch) + "\n")
    time.sleep(0.25)
