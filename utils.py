# -*- coding: UTF-8 -*-
import json


def json_to_dict(filename):
    with open(filename, 'r') as source:
        data = json.load(source)
    return data


def dict_to_json(data):
    with open('config.json', 'w+') as source:
        json.dump(data, source)


def print_dict(dictionary):
    for k, v in dictionary.keys():
        print(k, v, sep=": ")
