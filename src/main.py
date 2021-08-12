#! /usr/bin/env python3
# coding: utf-8

import sys
import socket
from connection import client_connect
from my_zappy_ia import zappy


def init_arguments():
    arguments = {}
    arguments["host"] = "127.0.0.1"
    arguments["port"] = 0000
    arguments["team_name"] = ""
    arguments["check_args"] = 0
    arguments["help"] = 0
    return arguments


def get_args():
    arg_list = []
    for arg in sys.argv:
        arg_list.append(arg)
    arg_list.pop(0)
    arguments = init_arguments()
    while arg_list:
        args = arg_list.pop(0)
        if args == "-help":
            arguments["help"] = 1
            arguments["check_args"] += 10
        elif args == "-p":
            arguments["port"] = int(arg_list.pop(0))
            arguments["check_args"] += 7
        elif args == "-n":
            arguments["team_name"] = arg_list.pop(0)
            arguments["check_args"] += 5
        elif args == "-h":
            arguments["host"] = arg_list.pop(0)
            arguments["check_args"] += 1
    return arguments


def handle_arguments(arguments):
    if arguments["check_args"] < 5:
        print("Please enter a port and a team name", file=sys.stderr)
        return 84
    elif arguments["check_args"] <= 6:
        print("Please enter a valid port", file=sys.stderr)
        return 84
    elif arguments["check_args"] <= 8:
        print("Please enter a team_name", file=sys.stderr)
        return 84
    return 0


def help():
    print("USAGE: ./zappy_ai -p port -n name -h machine")
    print("\tport is the port number")
    print("\tname is the name of the team")
    print("\tmachine is the name of the machine; localhost by default")


def main():
    arguments = get_args()
    if handle_arguments(arguments) == 84:
        return 84
    if arguments["help"] == 1:
        help()
        return 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((arguments["host"], arguments["port"]))
        if client_connect(arguments, s) == None:
            return
        zappy(s)


