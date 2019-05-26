#!/usr/bin/env python3

# Adafruit Raspberry Pi MPR121 Keyboard Example
# Author: Tony DiCola, Brennen Bearnes
#
# Allows you to turn touches detected by the MPR121 into key presses on a
# Raspberry Pi.
#
# Dependencies
# ============
#
# Make sure you have the required dependencies by executing the following commands:
#
#   sudo apt-get update
#   sudo apt-get install build-essential python-dev python-pip libudev-dev
#   sudo pip3 install python-uinput
#   sudo pip3 install adafruit-circuitpython-mpr121
#
# Usage
# =====
#
# To use this program you first need to connect the MPR121 board to the Raspberry
# Pi (either connect the HAT directly to the Pi, or wire the I2C pins SCL, SDA to
# the Pi SCL, SDA, VIN to Pi 3.3V, GND to Pi GND).
#
# Next define the mapping of capacitive touch input presses to keyboard
# button presses.  Scroll down to the KEY_MAPPING dictionary definition below
# and adjust the configuration as described in its comments.
#
# Finally run the script as root:
#
#   sudo python3 pi_keyboard.py
#
# Try pressing buttons and you should see key presses made on the Pi!  (Note
# that you need to be logged directly into the Pi to see the keypresses -
# over an SSH or console cable connection, you won't see anything.)
#
# Press Ctrl-C to quit at any time.
#
# Copyright (c) 2014-2019 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import logging
import time
import board
import busio
import adafruit_mpr121

# Key interrupter
NULL_CHAR = chr(0)

# Defined key press function
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

# Testing testing, Seth is gay!
# lol
# Keys
KEY_MAPPING = {
	0: (NULL_CHAR*2+chr(79)+NULL_CHAR*5),   # right arrow
	1: (NULL_CHAR*2+chr(81)+NULL_CHAR*5),   # down arrow
	2: (NULL_CHAR*2+chr(80)+NULL_CHAR*5),   # left arrow
	3: (NULL_CHAR*2+chr(82)+NULL_CHAR*5),   # up arrow
    4: (NULL_CHAR*2+chr(4)+NULL_CHAR*5),    # A
    5: (NULL_CHAR*2+chr(5)+NULL_CHAR*5),    # B
    6: (NULL_CHAR*2+chr(28)+NULL_CHAR*5),   # Y
    7: (NULL_CHAR*2+chr(27)+NULL_CHAR*5),   # X
}

# Sleep this long between polling for events:
EVENT_WAIT_SLEEP_SECONDS = 0.25

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)

# Event loop to wait for pin changes and respond to them.
print('i made a horrible keyboard [test phase]')
print('Press Ctrl-C to quit.')
last_touched = mpr121.touched()
while True:
    current_touched = mpr121.touched()
    for pin, key in KEY_MAPPING.items():
        if mpr121[pin].value:
            write_report(key)
        time.sleep(0.0001)
        if not current_touched & mpr121[pin].value and last_touched:
            write_report(NULL_CHAR*8)
    last_touched = current_touched