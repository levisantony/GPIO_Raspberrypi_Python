GPIO_Raspberrypi_Python
=======================

Controlling 6 GPIO ports using python code 

Install Debian in Rpi

RPi.GPIO Python library can help to control pins

  Follow steps to install Rpi.GPIO:
  
  Type the following commands in Terminal:-

1. wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.3.1a.tar.gz

2. tar zxf RPi.GPIO-0.3.1a.tar.gz

3. cd RPi.GPIO-0.3.1a

4. sudo python3 setup.py install

NB: Sometimes, this installation may fail. If yes, type "sudo apt-get install python3-dev".
    Then type "sudo python3 setup.py install"
    


Now copy the file named blink_leds.py to /home/pi

Type "sudo python3 blink_leds.py" in terminal, you can see the leds connected to the pins 11,12,13,15,16,18 blinking 
provided each led is grounded to pin 6.

