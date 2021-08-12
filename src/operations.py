#! /usr/bin/env python3
# coding: utf-8

import socket

BUFFER = 1024


def get_coord_from_case(item):
    line = 0
    column = 0 - line
    i = 0
    tmp = []
    case_nb = 0
    while item[i]:
        while column <= line:
            while item[i] and item[i][0] == case_nb:
                tmp.append(((column, line), item[i][1]))
                i += 1
            case_nb += 1
            column += 1
        line += 1
        column = 0 - line
    tmp.append(None)
    return tmp
