import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS=[15,17]


for i in PINS:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
    sleep(2)
    GPIO.output(i,GPIO.HIGH)
    
GPIO.cleanup()

