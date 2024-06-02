# Drone Image Transfer and Processing System
This repository is part of my MCE314 Mechatronics Engineering Design class. The goal of this project is to develop a system that processes images captured by a drone and sends them to a remote laptop for further analysis.

Project Overview

This project involves two main components:

Image Transfer:
This component is responsible for sending image data from the drone to the laptop.
The image transfer is performed using a simple HTTP command, which sends unprocessed images over a local network from an RPi (Raspberry Pi) mounted on the drone to the laptop.

Image Processing:
This component processes the images received on the laptop.
It uses OpenCV's color detection library to analyze the images.


