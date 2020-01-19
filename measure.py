#!/usr/bin/env python3
# coding: utf-8

from websocket_server import WebsocketServer
import RPi.GPIO as GPIO
import threading
import time
GPIO.setwarnings(False)

Trig = 19
Echo = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
GPIO.output(Trig, GPIO.LOW)

server = WebsocketServer(3000, "192.168.0.14")

def websocket_run():
    server.run_forever()

def main():
    websocket_thread = threading.Thread(target=websocket_run)
    websocket_thread.start()

    while True:
        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)
        while GPIO.input(Echo) == 0:
            signaloff = time.time()
        while GPIO.input(Echo) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff
        distance = round(timepassed * 17000)

        print(distance)

        server.send_message_to_all(str(distance))
        print("send")
        time.sleep(1)

main()
