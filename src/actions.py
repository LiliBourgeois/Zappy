#! /usr/bin/env python3
# coding: utf-8

from communications import get_object


def clear_the_case(s, inventory):
    i = 0
    while inventory[i]:
        data = get_object(s, inventory[i][0])
        while data == "ok\n":
            data = get_object(s, inventory[i][0])
        i += 1


def check_for_item(items, item):
    i = 0
    while items[i]:
        if items[i][1] == item:
            return items[i][0]
        i += 1
    return 0
