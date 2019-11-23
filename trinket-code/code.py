# Write your code here :-)
import busio
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=9600)

while True:
    data = uart.read()

    if data is not None:
        led.value = True
    else:
        led.value = False
