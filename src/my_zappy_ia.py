#! /usr/bin/env python3
# coding: utf-8

import socket
import time
from communications import look, get_inventory, move, get_object, broadcast
from get_direction import get_direction
from level_up import levelup_ceremony
from globals import getalive, getlevel


def get_prequisite_invoc():
    prequisit = {}
    prequisit["2"] = {
        "player": 1,
        "linemate": 1,
        "deraumere": 0,
        "sibur": 0,
        "mendiane": 0,
        "phiras": 0,
        "thystame": 0,
    }
    prequisit["3"] = {
        "player": 2,
        "linemate": 1,
        "deraumere": 1,
        "sibur": 1,
        "mendiane": 0,
        "phiras": 0,
        "thystame": 0,
    }
    prequisit["4"] = {
        "player": 2,
        "linemate": 2,
        "deraumere": 0,
        "sibur": 1,
        "mendiane": 0,
        "phiras": 2,
        "thystame": 0,
    }
    prequisit["5"] = {
        "player": 4,
        "linemate": 1,
        "deraumere": 1,
        "sibur": 2,
        "mendiane": 0,
        "phiras": 1,
        "thystame": 0,
    }
    prequisit["6"] = {
        "player": 4,
        "linemate": 1,
        "deraumere": 2,
        "sibur": 1,
        "mendiane": 3,
        "phiras": 0,
        "thystame": 0,
    }
    prequisit["7"] = {
        "player": 6,
        "linemate": 1,
        "deraumere": 2,
        "sibur": 3,
        "mendiane": 0,
        "phiras": 1,
        "thystame": 0,
    }
    prequisit["8"] = {
        "player": 6,
        "linemate": 2,
        "deraumere": 2,
        "sibur": 2,
        "mendiane": 2,
        "phiras": 2,
        "thystame": 1,
    }
    prequisit["all"] = {
        "player": 6,
        "linemate": 9,
        "deraumere": 8,
        "sibur": 10,
        "mendiane": 5,
        "phiras": 6,
        "thystame": 1,
    }
    return prequisit


def zappy(s):
    inventory = []
    prequisite_invoc = get_prequisite_invoc()
    while getalive():
        level = getlevel()
        items = look(s)
        inventory = get_inventory(s, inventory)
        direction = get_direction(prequisite_invoc, items, inventory, level)
        get_object(s, direction["object"])
        move(s, direction)
        levelup_ceremony(s, level, inventory, prequisite_invoc)
