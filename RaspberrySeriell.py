#!/usr/bin/python

import socket
import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)

se = serial.Serial('/dev/ttyAMA0', 9600) 
se.open()
time.sleep(5) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 50000
s.connect((host, port))
print ('Connected to', host)


while True:
    try:
        Temperatur = se.readline()
        PH-Wert = se.readline()
        Luftfeuchtigkeit = se.readline()
        print(Temperatur)
        print(PH-Wert)
        print(Luftfeuchtigkeit)
    except KeyboardInterrupt:
        se.close()   
    while True:
        s.send(bytes(Temperatur, "utf8"))
        s.send(bytes(PH-Wert, "utf8"))
        s.send(bytes(Luftfeuchtigkeit, "utf8"))
        a = str(s.recv(1024), "utf8")
        print(a)
        if a is "EIN" :
            GPIO.output(5, GPIO.HIGH)
        else:
            if a is "AUS" :
                GPIO.output(5, GPIO.LOW)
    
        
   
