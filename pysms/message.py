#!/usr/bin/env python
# coding=utf-8

import socket
import struct
import yaml


class MessageData:

    def __init__(self):
        self.host = '1'
        self.type = 'c'
        self.length = 0

class AppData:

    def load(self, data):
        self.data = yaml.load(data)
    
    def value(self, key):
        return self.data[key]

    def dump(self, data):
        return yaml.dump(data)
    

class Message:

    def __init__(self, port):
        self.host = '127.0.0.1'
        self.port = port
        self.node = 'log'

        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((self.host, self.port))

    def recv(self):
        data, addr = self.server.recvfrom(512)
        if (data):
            pack_str = "chc16si{0}s".format(len(data) - 28)
            recv_data = struct.unpack(pack_str, data)
            #for d in recv_data:
            #    print("{0}".format(d))
            #print("{0}".format(yaml.load(recv_data[5])))
        return recv_data[5]

    def send(self, data, to_addr):
        length = len(data)
        pack_str = "chc16si{0}s".format(length)
        print("{0}".format(pack_str))
        send_data = struct.pack(pack_str, b'\x68', length, b'N', b'127.0.0.1', 8899, data)
        #send_data = struct.pack('ss', 'c', 'c')
        self.server.sendto(send_data, to_addr)
