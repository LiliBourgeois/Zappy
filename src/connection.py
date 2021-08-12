#! /usr/bin/env python3
# coding: utf-8

import socket
from globals import setalive, getalive, setmessage, setlevel, getlevel, setm_direction


BUFFER = 1


def get_data(s):
    data = ""
    tmp = ""
    while "\n" not in tmp:
        tmp = s.recv(BUFFER).decode("utf8")
        data = data + tmp
    return data


def client_connect(arguments, s):
    data = get_data(s)
    team_name = arguments["team_name"] + "\n"
    s.sendall(team_name.encode("utf-8"))
    data = get_data(s)
    if "No more place in this team" in data:
        return None
    data = get_data(s)
    if "No more place in this team" in data:
        return None
    return s


def parse_message(data):
    x = data.split(",")
    x.append(None)
    tmp = x[0].split("-")
    if (tmp[0]):
        setm_direction(int(tmp[0]))
    tmp = x[1].split("-")
    if (tmp[1]):
        setmessage([tmp[1], tmp[1]])


def checkdata(s, data, command):
    if data == "dead\n":
        setalive(False)
        return None
    elif "message" in data:
        parse_message(data)
    elif "Elevation underway" in data:
        level = str(int(getlevel()) + 1)
        setlevel(level)
        pass
    elif "Current level:" in data:
        if command == "Incantation\n":
            return data
    elif data == "ok\n" or data == "ko\n":
        s.sendall(b"Connect_nbr\n")
        data2 = get_data(s)
        while data2 == "ok\n" or data2 == "ko\n":
            data2 = get_data(s)
        data2 = checkdata(s, data2, command)
        return data
    else:
        return data
    data = get_data(s)
    data = checkdata(s, data, command)
    return data


def send_command(s, command):
    if getalive() == False:
        return None
    s.sendall(command.encode("utf-8"))
    data = get_data(s)
    print("command = ", command, "data = ", data)
    data = checkdata(s, data, command)
    #print("second data = ", data)
    return data
