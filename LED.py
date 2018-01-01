import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PORT=16
PORT2=18
PORT3=21
DELAY=30;
YELLOW_DELAY=1

GPIO.setup(PORT,GPIO.OUT)
GPIO.setup(PORT2,GPIO.OUT)
GPIO.setup(PORT3,GPIO.OUT)

on=GPIO.HIGH

try:
    while(True):
        GPIO.output(PORT,on)
        time.sleep(YELLOW_DELAY)
        GPIO.output(PORT,not on)
        GPIO.output(PORT2,on)
        time.sleep(DELAY)
        GPIO.output(PORT2,not on)
        GPIO.output(PORT3,on)
        time.sleep(DELAY)
        GPIO.output(PORT3,not on)
except:
    GPIO.output(PORT3,not on)
    GPIO.output(PORT2,not on)
    GPIO.output(PORT,not on)
