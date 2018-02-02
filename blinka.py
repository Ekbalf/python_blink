import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23,GPIO.OUT)
    GPIO.output(23,GPIO.HIGH)

def blink():
    while True:
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23,GPIO.LOW)
        time.sleep(1)

def destory():
    GPIO.output(23,GPIO.LOW)
    GPIO.cleanup()

setup()
try:
    blink()
except:
    print"problem"
