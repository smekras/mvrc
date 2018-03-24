# -*- coding: UTF-8 -*-
import board
import motion


def show_pin_controls(mode):
    """
    Display the options for the state of pins,
    and ask the user to pick .

    :param mode: The mapping mode for the raspberry pi.
    :return: The function returns 1 if the pins are primed.
    """
    print("I: Prime Pins", "O: Reset Pins", sep="\n")
    choice = input("Enter choice: ").upper()
    if choice == "I":
        board.pin_handler("prime", mode)
        return 1
    else:
        board.pin_handler("reset", mode)
        return 0


def show_motor_controls():
    """
    Display the options for movement.

    :return: The function does not return anything.
    """
    key_list = motion.moves.keys()
    for entry in key_list:
        button = motion.moves[entry]["button"]
        print(button, entry, sep=": ")


def select_action():
    """
    Ask the user for desired action and select movement.

    :return: The function does not return anything.
    """
    action = input("Enter choice: ").upper()
    # TODO: add support for action to be set otherwise

    buttons = []
    for key in motion.moves.keys():
        button = motion.get_button(key)
        buttons.append(button)

    while action not in buttons:
        print("Invalid choice.")
        action = input("Enter new choice: ").upper()

    for button in buttons:
        for key in motion.moves.keys():
            if action == motion.moves[key]["button"]:
                motion.movement(key)


def main():
    """
    Ask the user to select mapping mode,
    then display pin and motor controls.

    :return: The function does not return anything.
    """
    mode = input("Select mode (BCM|BOARD)").upper()
    board.select_mode(mode)
    # TODO: add sensor controls
    if show_pin_controls(mode):
        show_motor_controls()
        select_action()


main()
