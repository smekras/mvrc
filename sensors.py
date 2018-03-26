# -*- coding: UTF-8 -*-
import time

import board

mapping = board.pin_map
es01 = board.pins["ESO1"][mapping]
esin = board.pins["ESIN"][mapping]
rs01 = board.pins["RSO1"][mapping]
rsin = board.pins["RSIN"][mapping]


def get_reflection():
    """
    Read the output of the infrared sensor and return it.

    :return: The function returns 1 if the surface is reflective.
    """
    while True:
        status = board.get_input(rsin)
        if status == 1:
            print("Reflective")
        else:
            print("Non-Reflective")
        time.sleep(0.1)
        # TODO: Replace text output with a simple return value
        return status


def get_distance():
    """
    Read the output of the ultrasonic sensor, and calculate the distance to the nearest object.

    :param sensor:
    :return: The function returns the distance to the nearest object.
    """
    ping_time = 0
    echo_time = 0
    if True:
        board.set_output(es01, "low")
        board.set_output(es01, "high")
        ping_time = time.time()
        time.sleep(0.00001)
        board.set_output(es01, "low")

        while board.get_input(esin) == 0:
            ping_time = time.time()
        while board.get_input(esin) == 1:
            echo_time = time.time()

        if (echo_time is not None) and (ping_time is not None):
            elapsed_time = echo_time - ping_time
            distance = elapsed_time * 17000
        else:
            distance = 0
        print("Ping: {ping_time} - Echo: {echo_time}")
        return distance


while True:
    stretch = get_distance()
    print(str(stretch) + "\n")
    time.sleep(0.25)
