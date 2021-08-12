#! /usr/bin/env python3
# coding: utf-8

from globals import getm_direction, getalive
from actions import clear_the_case
from communications import set_object, incant, look, broadcast, get_inventory
import time


def set_prequisite_invoc(prequisite_invoc, level, inventory, s):
    i = 1
    j = 0
    while inventory[i]:
        if j < prequisite_invoc[str(int(level) + 1)][inventory[i][0]]:
            set_object(s, inventory[i][0])
            j += 1
        else:
            j = 0
            i += 1


def enough_player(s, level, prequisite_invoc):
    items = look(s)
    i = 0
    playernb = 0
    while items[i] and items[i][0] == (0, 0):
        if items[i][1] == "player":
            playernb += 1
        i += 1
    if playernb >= prequisite_invoc[str(int(level) + 1)]["player"]:
        return True
    return False


def call_other_players(s, level, prequisite_invoc, inventory):
    broadcast(s, "Evolve-" + str(int(level) + 1) + "-")
    inventory = get_inventory(s, inventory)
    while enough_player(s, level, prequisite_invoc) == False and inventory[0][1] > 12:
        inventory = get_inventory(s, inventory)
        look(s)
        broadcast(s, "Evolve-" + str(int(level) + 1) + "-")


def levelup_ceremony(s, level, inventory, prequisite_invoc):
    if getalive() == False or getm_direction() != 10:
        return
    i = 1
    if inventory and inventory[0][1] < 6:
        return level
    if getm_direction() == 100:
        time.sleep(10)
        return level
    while inventory[i]:
        if prequisite_invoc[str(int(level) + 1)][inventory[i][0]] > inventory[i][1]:
            return level
        i += 1
    clear_the_case(s, inventory)
    if enough_player(s, level, prequisite_invoc):
        set_prequisite_invoc(prequisite_invoc, level, inventory, s)
        incant(s, level)
    else:
        call_other_players(s, level, prequisite_invoc, inventory)
        if inventory[0][1] < 2:
            return level
        else:
            set_prequisite_invoc(prequisite_invoc, level, inventory, s)
            incant(s, level)
    return level
