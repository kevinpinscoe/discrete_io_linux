# "Discrete I/O Programming in Linux"

Combined with my book "Discrete I/O Programming in Linux" (publishing pending) are some code examples of my experiments into the subject.

This is a work in progress.

## Why discrete I/O?

There are many applications for this but first an explanation of what Discrete I/O is and isn't.

Discrete I/O is sending and receiving digital signals external to a computer which are binary in nature meaning on of off. For example, a discrete input would sense the position of a switch; a discrete output would turn on a pump or light.

## Applications

There are many applications such as sensing of water is present above a certain line such as in a basement. It can be used in Ham Radio to sense when a antenna rotor is past a certain point or at a stop. You csn remotely turn on a device like a ham radio. A switch can be made to sense when an analog action such as humidity has reached a certain point and turns of a switch for a specified action. And of course a discrete can be used in a property alarm to detect an open door or a broken window which would then raise an alarm. Another use is to connect a model railroad and sense when a car has passed through a point on the track in which to lower a bridge or light up a signal. Tools such as Node-RED (https://nodered.org/) can be used to wire all this together. 

## Why discrete?

Another type of computer input would be analog. An analog input would have a value to it such as a temperature reading or a water level. While this value would be vary useful it may be too complex and more expensive to provide values both in the interface and in the measuring device. Discrete provides an economical way of signaling when a simple solution or single state is required. 

## Why Linux?

It is open source, easy to work with, freely available and can work in a small foot print such as Raspberry Pi's.

## Sample uses

TBA

## Interfaces

There are discrete I/O boards you can buy for a Linux PC that have many inputs but I will focus here on already present hardware in most PC's such as the RS-232 serial port and the Universal Serial Bus known as "USB". Legacy PC's had additional ports that could be used for discrete such as PS/2, Centronics style parallel printer ports and IEEE 139 (Firewire) ports but they are long out of manufacture so I wont cover them here. Note that te Raspberry Pi has many discrete I/O options available including General-Purpose Input/Output (GPIO) which we will cover in later chapters. If you are interested in using the parallel port and you have the hardware still around I suggest reading Linux Device Drivers, Second Edition by O'Reilly. A note on special discrete I/O boards. I have worked in the past with special somewhat expensive discrete I/O and coded and modulated timing controlled Inter-range instrumentation group (IRIG) boards. I wont cover that here either since this is covered elsewhere. This work covers simply off the shelf, readily available and commodity based PC computers.

## Non-Linux

There are off the shelf discrete I/O devices such as the smartDEN IoT MQTT Ethernet 16 Relay Module - DIN RAIL BOX (https://denkovi.com/smartden-iot-mqtt-ethernet-16-relay-module-din-rail-box) but these requite MQTT or so e other messaging software the communicate.  
