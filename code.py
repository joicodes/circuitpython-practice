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
from random import choice

# The RGB values:
BLACK   = (0,0,0)
WHITE   = (255,255,255)   
RED     = (255, 0, 0)
MAGENTA = (255,0,255)
BLUE    = (0, 0, 255)
CYAN    = (0,255,255)
GREEN   = (0,255,0)
YELLOW  = (255,255,0) 

color_list = [RED, WHITE, MAGENTA, BLUE, CYAN, GREEN, YELLOW]


#💡 NeoPixels - 10 built in 10 RGB NeoPixel LEDs.
# Colors are set in the form of an (R, G, B) tuple. 
# NeoPixel Helper Functions (use cpx.pixels):
def change_color(color, index=None):
    '''
    Changes the RGB color of a given NeoPixel. \n
    If index exceeds number of pixels, changes all pixels to given color.
    If index is not passed, changes all pixels to given color. 
    '''
    if index == None or index >= len(cpx.pixels):
        cpx.pixels.fill(color)
    else:
        cpx.pixels[index] = color

def blink_color(color, time=0.5):
    '''Flashes a given color, for a given number of seconds'''
    change_color(color)
    sleep(time)
    change_color()
    sleep(time)


#🚨 D13 - red LED (D13) next to the USB port.
# 'on' and 'off' are states are True and False.
# D13 Helper Functions (Use cpx.red_led):
def blink_red_led(time=0.5):
    '''Flashes a given color, for a given number of seconds'''
    cpx.red_led = True
    sleep(time)
    cpx.red_led = False
    sleep(time)


#🎚 D7 - side swich above the battery connector.
# 'on' and 'off' are states are True and False.
# D7 Helper Functions (Use cpx.red_led):


# Built in accelerometer functionality:

#👆 Tap Detection - options: single tap, double tap
# Tap Helper Functions (Use cpx.tapped)

# Example: cpx.tapped


#🤝 Shake Detection - options: shake_threshold (int)
# Default Threshold:shake_threshold = 30
# Lowest (more sensitive): shake_threshold = 10
# Shake Helper Functions (Use cpx.shake())

# Example: cpx.shake(shake_threshold=20)

#TODO: https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/light
#🌞 A8 Light Detection - light sensor
# Default Threshold:shake_threshold = 30
# Lowest (more sensitive): shake_threshold = 10
# Shake Helper Functions (Use cpx.shake())

# Example: cpx.shake(shake_threshold=20)



# Initialize Settings:
cpx.pixels.brightness = 0.1
cpx.detect_taps = 1  # Pre-set for double tap detection
on = True

while True:

    # D13 on when switch is on.
    cpx.red_led = cpx.switch

    if cpx.tapped:
        current_color = choice(color_list)
        change_color(current_color)
