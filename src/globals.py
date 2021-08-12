#! /usr/bin/env python3
# coding: utf-8


alive = True
message = None
m_direction = 10
level = "1"


def getalive():
    return globals()["alive"]


def setalive(isalive):
    globals()["alive"] = isalive


def getmessage():
    return globals()["message"]


def setmessage(newmessage):
    globals()["message"] = newmessage


def getm_direction():
    return globals()["m_direction"]


def setm_direction(newm_direction):
    globals()["m_direction"] = newm_direction


def getlevel():
    return globals()["level"]


def setlevel(new_level):
    globals()["level"] = new_level
