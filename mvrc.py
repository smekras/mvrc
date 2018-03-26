# -*- coding: UTF-8 -*-
import board
import motion


def main():
    if board.pin_map is not "BCM":
        board.map_pins()
    if board.pin_control is not "prime":
        board.control_pins()
    else:
        board.set_pins(board.pin_control)
    motion.show_controls()
    motion.select_movement()


main()
