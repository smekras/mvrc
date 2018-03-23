# -*- coding: UTF-8 -*-
import move as move


def show_controls():
    keylist = move.moves.keys()
    for entry in keylist:
        button = move.moves[entry]["button"]
        print(button, entry, sep=": ")


show_controls()
