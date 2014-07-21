#!/usr/bin/env python
# coding=utf-8

import sys

sys.path.append('../')

from pysms.message import Message, AppData

if __name__ == "__main__":

    msg = Message(8899)
    app_data =  AppData()
    data = {'name':'cnsworder',
            'type' : 'cmd'   }

    while (True):
        send_data = "cmd:log\ninfo:mylog\n\n"#data.dump(data)
        #s = app_data.load(send_data)
        msg.send(send_data, ("127.0.0.1", 9988))
