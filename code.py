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

def fill_all(color):
    '''Fills all NeoPixel with given color'''
    cpx.pixels.fill(color)

while True:
    # start your code here

   
    # To control what happens when things are on and off
    # You can use cpx.switch:


    # To make it simulate blinking, we use sleep():
    on = True

    if cpx.switch == on:
        fill_all(RED)
        sleep(1)
        fill_all(BLACK)
        sleep(1)
    else:
        cpx.pixels.fill(BLACK)
