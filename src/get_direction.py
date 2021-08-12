#! /usr/bin/env python3
# coding: utf-8

from actions import check_for_item
from globals import setmessage, getmessage, setm_direction, getm_direction, getalive
from random import randint


def get_direction(prequisite_invoc, items, inventory, level):
    if getalive() == False:
        return
    direction = {
        "front": randint(0, 3),
        "left": randint(0, 3),
        "right": randint(0, 3),
        "object": "",
    }
    i = 1
    if getmessagecheck(getmessage(), level) != False:
        direction = get_message_direction(getm_direction(), level, items)
        return direction
    while inventory != [None] and inventory[i]:
        if prequisite_invoc[str(int(level) + 1)][inventory[i][0]] > inventory[i][1]:
            dest = check_for_item(items, inventory[i][0])
            if dest != 0:
                direction = choose_direction(dest, direction)
                direction["object"] = inventory[i][0]
        elif prequisite_invoc["all"][inventory[i][0]] > inventory[i][
            1
        ] and direction == {"front": 2, "left": 0, "right": 0, "object": ""}:
            dest = check_for_item(items, inventory[i][0])
            if dest != 0:
                direction = choose_direction(dest, direction)
                direction["object"] = inventory[i][0]
        i += 1
    return direction


def getmessagecheck(message, level):
    if getmessage() == None:
        return False
    if message[0] != "Evolve" or message[1] != str(int(level) + 1):
        return False
    return True


def get_message_direction(m_direction, level, items):
    direction = {"front": 0, "left": 0, "right": 0, "object": ""}
    if m_direction == 0:
        setmessage(None)
        setm_direction(100)
        return direction
    elif m_direction == 1:
        direction["front"] = 1
    elif m_direction == 2:
        direction["front"] = 1
        direction["left"] = 1
    elif m_direction == 8:
        direction["front"] = 1
        direction["right"] = 1
    elif m_direction == 3 or m_direction == 4 or m_direction == 5:
        direction["left"] = 1
    elif m_direction == 6 or m_direction == 7:
        direction["right"] = 1
    setmessage(None)
    setm_direction(10)
    return direction


def choose_direction(dest, direction):
    direction["front"] = dest[1]
    if dest[0] < 0:
        direction["left"] = dest[0]
    elif dest[0] > 0:
        direction["right"] = dest[0]
    return direction
