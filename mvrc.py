# -*- coding: UTF-8 -*-
import pins


def show_pin_controls():
    print("I: Prime Pins", "O: Reset Pins", sep="\n")
    choice = input("Enter choice: ").upper()
    if choice == "I":
        pins.pin_handler("prime")
        return 1
    else:
        pins.pin_handler("reset")
        return 0


def show_motor_controls():
    key_list = pins.moves.keys()
    for entry in key_list:
        button = pins.moves[entry]["button"]
        print(button, entry, sep=": ")


def select_action():
    buttons = []
    for key in pins.moves.keys():
        button = pins.get_button(key)
        buttons.append(button)

    action = input("Enter choice: ").upper()
    while action not in buttons:
        print("Invalid choice.")
        action = input("Enter new choice: ").upper()

    for button in buttons:
        for key in pins.moves.keys():
            if action == pins.moves[key]["button"]:
                pins.movement(key)


def main():
    # TODO: add sensor controls
    if show_pin_controls():
        show_motor_controls()
        select_action()


main()
