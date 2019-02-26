#!/usr/bin/python

import socket
minTemp = (int(str(input("Minimale Temperatur"))))
#minTemp = (int(str(f1)))
maxLuft = (int(str(input("maximale Luftfeuchtigkeit"))))
#maxLuft = (int(str(j1)))
maxPH = (int(str(input("Maximaler PH-Wert"))))
#maxPH = (int(str(k1)))

u = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8008
u.bind((host, port))
u.listen(5)
c = None
while True:
   if c is None:
       # Halts
       print ('[Waiting for connection...]')
       c, addr = u.accept()
       print ('Got connection from', addr)
   else:
       #print ('[Waiting for response...]')
       a = str(c.recv(1024), "utf8")
       print ("Aktuelle Temperatur", a)
       b = (float(str(a)))
       if b >minTemp:
           g = str(c.recv(1024), "utf8")
           d = (float(str(g)))
           print("Aktueller PH-Wert",d)
           if d < maxLuft:
               v = str(c.recv(1024), "utf8")
               w = (float(str(v)))
               if w < maxPH :
                   e = "EIN"
                   print(e)
                   c.send(bytes(e, "utf8"))
               else:
                   h = "AUS"
                   print(h)
                   c.send(bytes(h, "utf8"))
               
           else:
               str(c.recv(1024), "utf8")
               f = "AUS"
               print(f)
               c.send(bytes(f, "utf8"))
       else:
           str(c.recv(1024), "utf8")
           g = "AUS"
           print(g)
           c.send(bytes(g, "utf8"))
       
