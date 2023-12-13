# GPIO program examples for a Raspberry Pi

These were tested on the new Raspberry Pi 5.

Because of this new hardware I am moving away from the RPi.GPIO Python library to the 
gpizero library (https://gpiozero.readthedocs.io/en/latest/).

The gpiozero library refers to buttons (input) and led's (output) rather than pins.

The mapping of the pins to led's or buttons can be found at https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins 

So to turn on LED number 2 you would connect a LED in a bread board with GND pin and pin 2 in series with a 330 ohm resistor. Never connect a LED directly to the GPIO pins.

Likewise if you want a button action as an input connect the ground pin on a breadboard with a micro switch in series with a 330 ohm resistor and say pin 2. Again never connect a switch directly to the GPIO pins without a current limiting resistor. 

## Script examples

- led_pulse.py - Turn LED number 2 on and off every two seconds