#!/usr/bin/python
 
import RPi.GPIO as GPIO
import os, time

gpio_pin_number=20
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Monitoring pin {pin} for shutdown".format(gpio_pin_number))

def shutdown:
   print("Shutdown request detected")
   os.system("sudo shutdown -h now")

try:
   while True:
      if (GPIO.input(gpio_pin_number) == GPIO.LOW):
         shutdown()
         break
      time.sleep(1)
except KeyboardInterrupt:
   print('Stoped')

GPIO.cleanup()
