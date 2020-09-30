"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# Import CPX Library
from adafruit_circuitplayground.express import cpx
from time import sleep

# The RGB values:
BLACK   = (0,0,0)
WHITE   = (255,255,255)   
RED     = (255, 0, 0)
MAGENTA = (255,0,255)
BLUE    = (0, 0, 255)
CYAN    = (0,255,255)
GREEN   = (0,255,0)
YELLOW  = (255,255,0) 


def change_pixel(index, color):
    '''Changes the RGB color of a given NeoPixel.'''
    cpx.pixel[index] = color

def fill_pixels(color):
    '''Fills all NeoPixel with given color.'''
    cpx.pixels.fill(color)

def lights_out():
    '''Fills all NeoPixels black.'''
    cpx.pixels.fill(BLACK)

def blink_color(color, time=0.5):
    '''Flashes a given color, for a given number of seconds'''
    fill_pixels(color)
    sleep(time)
    lights_out()
    sleep(time)

while True:

    on = True

    if cpx.switch == on:
        blink_color(CYAN, 1)
    else:
        fill_pixels(BLACK)
