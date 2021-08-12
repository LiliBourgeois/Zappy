#! /usr/bin/env python3
# coding: utf-8

import socket
from operations import get_coord_from_case
from connection import send_command
from globals import getalive
import time


def look(s):
    if getalive() == False:
        return
    item = []
    data = send_command(s, "Look\n")
    if data == None or data == "ok\n" or data == "ko\n" or data ==[None]:
        item.append(None)
        return item
    if "[" not in data or " ]" not in data:
        return look(s)
    x = data.split(",")
    x.append(None)
    i = 0
    while x[i]:
        tmp = x[i].split(" ")
        tmp.append(None)
        j = 0
        while tmp[j] != None:
            if tmp[j] != "[" and tmp[j] != "]\n" and tmp[j] != "":
                item.append((i, tmp[j]))
            j += 1
        i += 1
    item.append(None)
    item = get_coord_from_case(item)
    return item


def get_inventory(s, inventory):
    if getalive() == False:
        return
    data = send_command(s, "Inventory\n")
    if data == None or data == "ok\n" or data == "ko\n":
        return inventory
    if "[ food " not in data or " ]" not in data:
        return get_inventory(s, inventory)
    tmp_inventory = []
    x = data.split(",")
    x.append(None)
    i = 0
    while x[i]:
        tmp = x[i].split(" ")
        if len(tmp) >= 3:
            tmp_inventory.append((tmp[1], int(tmp[2])))
        else:
            return inventory
        i += 1
    tmp_inventory.append(None)
    return tmp_inventory


def move(s, direction):
    if getalive() == False:
        return
    i = 0
    turn = None
    while i != direction["front"]:
        get_food(s)
        data = send_command(s, "Forward\n")
        i += 1
    i = 0
    if direction["right"] > 0:
        data = send_command(s, "Right\n")
        turn = "right"
    elif direction["left"] > 0:
        data = send_command(s, "Left\n")
        turn = "left"
    while turn != None and i != direction[turn]:
        get_food(s)
        data = send_command(s, "Forward\n")
        i += 1


def incant(s, level):
    if getalive() == False:
        return
    data = send_command(s, "Incantation\n")
    if data == None or data == "ko\n":
        return level
    return str(int(level) + 1)


def get_food(s):
    if getalive() == False:
        return
    data = send_command(s, "Take food\n")
    foodnb = 0
    while data == "ok\n" and foodnb < 7:
        data = send_command(s, "Take food\n")
        foodnb += 1


def get_object(s, object):
    if getalive() == False:
        return
    object = "Take " + object + "\n"
    data = send_command(s, object)


def set_object(s, object):
    if getalive() == False:
        return
    object = "Set " + object + "\n"
    data = send_command(s, object)


def broadcast(s, message):
    if getalive() == False:
        return
    command = "Broadcast " + message + "\n"
    data = send_command(s, command)
