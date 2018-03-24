# Most Vexing RoboCar (MVRC)
This repository holds the code for a RoboCar project. The project was originally conceived as an assignment for the first semester of the "IT Technology" AP Degree of Business Academy Aarhus, for 2018 (ITEK_f118v).

## Collaborators
* Stergios Mekras - (eaasmek) | smekras
* Cristian-Marian Radu - (eaacmra) | caticu
* Francis Kwame Fianyo - (eaafkf) | fKwame

## Files
* **board.py:** Python file containing pin-related code
* **motion.py:** Python file containing motion-related code
* **mvrc.py:** Python file containing the  main code of the project
* **sensors.py:** Python file containing sensor-related code
* **README.md:** This file

## Installation
### Hardware
In order for this code to be run and tested, a fully functional Raspberry Pi is needed, along with additional hardware.
The items below are only for reference. Any compatible and comparable model should work.
* **Board:** A "Raspberry Pi 3 Model B", with an 8GB SSD card, was used for this project.
* **Ultrasonic sensor:** A "SparkFun Ultrasonic Distance Sensor" (HC-SR04) was used for this project.
* **Infrared sensor:** A "SparkFun RedBot Sensor - Line Follower" (QRE1113) was used for this project.
* **H-Bridge:** A "SparkFun Motor Driver - Dual TB6612FNG" (with Headers) was used for this project.
* **DC Motor:** Four "DAGU Off set motor accessories 1:48", part of a "DG012-ATV 4WD (ATV) Multi Chassis Kit"
package, were used for this project. 
### Software
The latest version of Rasbian (Rasbian Stretch Lite - March 2018) is recommended,
but any version that supports the following packages will suffice, and they should be installed.
Other necessary packages are either already installed in the distribution, or will be pulled by these.
#### apt-get install:
* python3-pip
* apache2
* php
#### pip install:
* RPi.GPIO
#### manual install:
* wiringPi
