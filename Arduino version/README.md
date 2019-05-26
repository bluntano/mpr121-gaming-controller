# USB HID Capacitive Touch Gaming Controller based on Arduino board with USB master support in it

A gaming controller that actually works (unlike the Python and Raspberry Pi Zero version)

## What hardware does it use?

Here's the list of what hardware is used to make this work:
- Arduino board with a chip that has native USB HID support built in it, such as:
	- ATmega32u4
	- ATmega328P (*on some boards at least?*)
	- ATSAMD series
- A [capacitive touch sensor](https://www.adafruit.com/product/2340) (in my case I used Capacitive Touch Sensor HAT for Raspberry Pi by Adafruit, MPR121)
- Punch of crocodile wires to attach the conductive objects to the sensor
- micro-USB to USB cable

## What do I need in code- or software-wise?

You'll need:
- A bit of soldering skills (doesn't matter on which MPR121 sensor, you'll need to get some hands dirty.)
- Adafruit's MPR121 Arduino library:
   - Source code is on Github, can be found [here!](https://github.com/adafruit/Adafruit_MPR121)
   - Tutorial on how to setup the sensor on Arduino. Also, no need to worry about if they used the breakout version of MPR121 sensor. The instructions remain the same. The turial can be found [here!](https://learn.adafruit.com/adafruit-mpr121-12-key-capacitive-touch-sensor-breakout-tutorial/pinouts)

Also a QUICK NOTE regarding to SparkFun Pro Micro users, maybe some of you are, idk:

- Here's the full stuff about a lot of stuff covered [here!](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide/all) But I do wanna mention real quick:
	- Make sure you give a little tab of superglue under the micro-USB port. Pro Micros have this tendency to have micro-USB to break off due to very bad soldering
	- **MAKE SURE YOU CHOOSE THE RIGHT PROCESSOR IN ARDUINO IDE BEFORE UPLOADING THE CODE ONTO THE BOARD!!!** If you have a 5V/16MHz processor, **CHOOSE THAT VERSION OR YOU'LL BRICK THE BOARD!!!** On default it is set on 3.3V 8MHz version so, to change that, go to your Arduino IDE, choose Tools -> Processor -> ATmega32U4 (5V/16MHz) or (3.3V/8Mhz)
	- If your Pro Micro stops working all of a sudden and you've followed those two above things, don't worry! Mine stopped working and, I'm trying to figure out why. Only the power LED is on when plugged in.

I used the MPR121 Cap. Touch HAT sensor on my SparkFun Pro Micro board and I connnected jumper wires accordingly:
- SDA -> D2
- SCL -> D3
- 3.3V -> VCC (5V gave me I think grounding issues? The sensor went apeshit)
- GND -> GND
   
## Any additional material I could use?

How to install libraries on Arduino IDE in [here](https://www.arduino.cc/en/Guide/Libraries) and some knowledge of C++ (Arduino version, should not be too hard)

## Does this thing actually work?

YES!!! It's a **MASSIVE** improvement over the Raspberry Pi Zero (W) version, the difference is night and day. Since some of the Arduino boards have Keyboard.h library, it is definitely worth of using Arduino solution instead. Raspberry Pi did input but, it can only input predefined keystrokes and key macros, which is good enough for Python and Raspberry Pi. There were like minor bugs with the sensor where it randomly stopped registering touches but, that issue mostly lies under the sensor issue. I achieved my goal of making a motherfuckin cardboard gaming controller with punch of nails. Holy shit! FINALLY!!! :3

Have a nice day. Peace out, playas! :)
