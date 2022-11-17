#Write a python code for blinking LED and traffic lights for raspberry pi.

#Code for Blinking LED :

import RPi.GPIO as GPIO
import time
LED = 40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
While True:
 GPIO.output(LED,GPIO.HIGH)
 Time.sleep(1)
 GPIO.output(LED,GPIO.LOW)
 Time.sleep(1)


#Code for Traffic lights :

from gpiozero import Button,Trafficlights,Buzzer
from time import sleep
buzzer = Buzzer(15)
button = Button(21)
lights = Trafficlights(25,8,7)
while True:
 button.wait_for_press()
 buzzer.on()
 light.green.on()
 sleep(1)
 lights.amber.on()
 sleep(1)
 lights.red.on()
 sleep(1)
 lights.off()
 buzzer.off()