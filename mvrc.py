# -*- coding: UTF-8 -*-
import move as move


def show_pin_controls():
    print("I: Prime Pins", "O: Reset Pins", sep="\n")
    choice = input("Enter choice: ")
    if choice == "I":
        move.pin_handler("prime")
        show_motor_controls()
    else:
        move.pin_handler("reset")


def show_motor_controls():
    key_list = move.moves.keys()
    for entry in key_list:
        button = move.moves[entry]["button"]
        print(button, entry, sep=": ")


def select_action():
    buttons = []
    for key in move.moves.keys():
        button = move.get_button(key)
        buttons.append(button)

    action = input("Enter choice: ").upper()
    while action not in buttons:
        print("Invalid choice.")
        action = input("Enter new choice: ").upper()

    for button in buttons:
        for key in move.moves.keys():
            if action == move.moves[key]["button"]:
                return key


def main():
    show_pin_controls()
    choice = select_action()
    move.movement(choice)


main()
