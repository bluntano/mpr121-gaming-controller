# USB HID Capacitive Touch Gaming Controller based on Raspberry Pi Zero/Zero W

**Spoiler Alert:** that version sucks ass. Better use Arduino board for keyboard/controller case! Sorry.
A gaming controller. Inputs keys whether they are numbers, letter, misc keys, function keys, etc.

## What hardware does it use?

Here's the list of what hardware is used to make this work:
- Raspberry Pi [Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/) or [Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) (they both should work since they both have an extra data micro-USB port)
- A [capacitive touch sensor](https://www.adafruit.com/product/2340) (in my case I used Capacitive Touch Sensor HAT for Raspberry Pi by Adafruit, MPR121)
- Punch of crocodile wires to attach the conductive objects to the sensor
- A memory card (for operating system, and basically for the whole thing to work, min. 8 GB)
- micro-USB to USB cable

## What do I need in code- or software-wise?

Since this repository comes with only the USB keyboard Python script, you will need:
- Adafruit's MPR121 CircuitPython library:
   - Source code is on Github, can be found [here!](https://github.com/adafruit/Adafruit_CircuitPython_MPR121)
   - Tutorial on how to setup the sensor in Raspberry Pi. Also, no need to worry about if they used the breakout version of MPR121 sensor. The instructions remain the same. The turial can be found [here!](https://learn.adafruit.com/adafruit-mpr121-12-key-capacitive-touch-sensor-breakout-tutorial/overview)
- Setting up Raspberry Pi Zero/Zero W as a USB HID device. That tutorial can be found [here!](https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/) Everything should be covered in that tutorial.

## Any additional material I could use?

Yes! A USB HID usage table which can be found [here.](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf) Keyboard codes can be found in "10 Keyboard/Keypad Page (0x07)" at page 53.

## Does this thing actually work?

Yes and big no. It works as in it inputs the keys (e.g.: you press an apple, it inputs letter S) but, you have low control over it. In games it did not work as I wished for. I experienced constant twitching and not moving practically at all. I'm not entirely sure if it's the problem with Raspberry Pi that it cannot provide key inputs enough that the movement or input would be flawless, or if it's the Python code that is restricted in any possible way. Or is it not designed for the keyboard purpose at all, and instead is meant for to press sequence of keys at once, like key macros. Either way, I haven't given up yet and, want to carry on with it to make it better or think of some other possible solution. 

If you can figure it out, please let me know as well. It would be highly appreciated. If I left something uncovered in here, I'm sorry.

Have a nice day. Peace out, playas! :)
