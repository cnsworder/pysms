#!/usr/bin/env python
# coding=utf-8

import sys

sys.path.append('../')

from pysms.message import Message, AppData

if __name__ == "__main__":

    msg = Message(9988)
    app = AppData()

    while (True):
        data = msg.recv()
        print("{data}".format(data=data.decode()))
