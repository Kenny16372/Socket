#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host1 = ''
host2 = ''
port1 = 50000
port2 = 8008
s.connect((host1, port1))
print ('Connected to', host1)
t.connect((host2, port2))
print ('Connected to', host2)
while True:
    a = str(s.recv(1024), "utf8")
    print(a)
    t.send(bytes(a, "utf8"))
    b = str(s.recv(1024), "utf8")
    print(b)
    t.send(bytes(b, "utf8"))
    c = str(s.recv(1024), "utf8")
    print(c)
    t.send(bytes(c, "utf8"))
    d = str(t.recv(1024), "utf8")
    print(d)
    s.send(bytes(d, "utf8"))
    
