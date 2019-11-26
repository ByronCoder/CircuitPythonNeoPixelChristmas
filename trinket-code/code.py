# Write your code here :-)

import time
import board
import neopixel
import supervisor
import sys

pixel_pin = board.D0
num_pixels = 12
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

while True:
    if supervisor.runtime.serial_bytes_available:
        incomingByte = sys.stdin.readline().rstrip()
        print("incomingByte: " + str(incomingByte))
        if incomingByte is not None:
            alpha = float(int(incomingByte) / 100)
            for i in range(num_pixels):
                pixels[i] = (int(255 * alpha), int(0 * alpha), int(255 * alpha))
                pixels.show()
    else:
        for i in range(num_pixels):
            pixels[i] = (0, 0, 0)
            pixels.show()
        print("hit else")