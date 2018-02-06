# Red Robotics Headboard V1.2 (Beta)

Python library for the Red Robotics 'HeadBoard' Raspberry Pi add on robotics board.

Simple python commands for controlling motors, servos and Neopixels (WS2812B).

Drive a robot with a variety of controllers with example code for Rock Candy and PiHut PS3 Gamepads, Wiimote and generic bluetooth gamepads.  
Get a robot up and running in minutes!

This guide assumes a working knowledge of the Raspberry Pi and how to set one up headlessly.

Beginner video tutorials coming soon.




## Installation:

It's best to start with a fresh install of Raspian Lite. 
Download it from the [Raspberry Pi](https://www.raspberrypi.org/downloads/) website.

Pre-configured SD card image coming soon. 


Set up your Pi and connect it to your Wifi network.
Here's a great guide on how to do it from [Adafruit](https://learn.adafruit.com/raspberry-pi-zero-creation/overview).


Once your Pi is up and running, make sure everything is up to date by copying and pasting the following in the terminal:

`sudo apt-get update && sudo apt-get upgrade -y`


When that's finished, copy and paste:

`curl -L https://raw.githubusercontent.com/RedRobotics/HeadBoard/master/setup.sh | bash`

This will install all the files you need, your Pi will reboot when the installation is finished.


## What's my IP address?
If you have successfully connected to a wireless network, once your Pi has booted up it will flash the last three digits of it's IP address on the on-board Neopixel.  

If your IP address is 192.168.1.123, the Neopixel will flash red once, green twice and blue three times.  
If your IP address is 192.168.1.108, the Neopixel will flash red once then blue eight times.

If you miss it, you can press the on-board push button to flash the IP address again (wait a few seconds after pressing the button).

The first part of the address will be the same as the computer you are using to remotely connect to the Pi.
On a Linux PC, in the terminal type:
`ifconfig` 


## Quick Start Guide To Controlling A Robot


## Basic Libray Usage:

Open up a python shell with:  
`sudo python`

Load the neopixel module:  
`from neopixels import *`  
Wait for the neopixels module to load (It can take a few seconds).


To set the on-board neopixel to full red type:

`red()`

You can also set the brightness by adding number between 0-255, eg. half bright:

`red(127)`

This also works with blue and green and white:

`blue()`

`green()`

`white()`

If you want different colours, use:  
`setColour(0,128,0,128)`  
This will give you purple. The first value is the position of the neopixel (0 for the one on the Headboard).  
The next three numbers are the red, green and blue values.

Orange:  
`setColour(0,255,165,000)`

Yellow:  
`setColour(0,255,255,0)`  
    
### Other neopixel commands

You can fade red up and down with:  
`heartbeat()`
__Ctrl + c__ to stop

Attach more Neopixels to the 3pin header, pin closest to the led is +v then Data then Ground. 

With eight led's attached - try:  
`knightrider()`
__Ctrl + c__ to stop


To turn all neopixels off:  
`clear()`  

  

## Motors

`from headboard import *`

Motor1 full speed forwards:  
`M1(100)` 

Motor1 half speed forwards:  
`M1(50)`

Motor1 full speed backwards:  
`M1(-100)`

Motor1 stop:  
`M1(0)`

Motor2 full speed forwards:  
`M2(100)`

Motor2 stop:  
`M2(0)`

If you prefer, you can use 8 bit values (0-255) to set the speed. This is useful if you are using analogue joysticks to control your robot. You can send the value read from the joystick straight to the motor.  
See the Rock Candy and PiHut PS3 programs for examples.

Motor1 full speed:  
M1_255(255)

Motor2 half speed:  
M2_255(127)

Motor2 half speed Backwards:
M2_255(-127)



## Hobby Servo motors

`from headboard import *`

You can connect two servos - servo0 and servo1

Set the angle of the servo directly - to set the servo to the centre position:  
`servo0(0)`

Or for servo1:  
`servo1(0)`

90 degrees:  
`servo0(90)`

-45 degrees  
`servo0(-45)`

If you prefer, you can set the servo position by the pulse width.
Minimum value is 500, max is 2500.

Centre:  
`servo0_P(1500)`

+90 degrees:  
`servo0_P(500)`

-45 degrees:  
`servo0_P(2000)`

-90 degrees:  
`servo0_P(2500)`

Cut the power to the servo with:  
`servo0_off()`

## Reset/Shutdown switch

Short press- less than a second: LED will just flash yellow

Medium press - between 1 and 4 seconds: LED turns orange - Pi resets

Long press - greater than 4 seconds: LED turns red - Pi shutsdown


Wait 20 seconds before sliding the power switch to make sure the Pi has had enough time to shutdown.
