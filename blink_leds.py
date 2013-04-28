#python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# Setting pins(11,12,13,15,16,18) as output
print("Setup Pin 11,12,13,15,16,18")
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

var=1
print("Start Blinking")
while var==1 :
  print("Leds OFF")
  GPIO.output(11, False)
  GPIO.output(12, False)
  GPIO.output(13, False)
  GPIO.output(15, False)
  GPIO.output(16, False)
  GPIO.output(18, False)
  time.sleep(1)
  print("Leds On")
  GPIO.output(11, True)
  GPIO.output(12, True)
  GPIO.output(13, True)
  GPIO.output(15, True)
  GPIO.output(16, True)
  GPIO.output(18, True)
  time.sleep(1)
