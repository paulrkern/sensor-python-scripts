#!/usr/bin/env python
import RPi.GPIO as GPIO

TiltPin = 11

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
	GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def alert(ev=None):
        print("#####################################")
        print("#           TILT DETECTED           #")
        print("#####################################")

def loop():
        GPIO.add_event_detect(TiltPin, GPIO.FALLING, callback=alert, bouncetime=100) #callback=swLed, bouncetime=100) # wait for falling
        while True:
                pass # Don't do anything

def destroy():
        print("#####################################")
        print("#           CTRL+C DETECTED          ")
        print("#####################################")
        GPIO.cleanup() # Release resource

if __name__ == '__main__':     # Program start from here
        setup()

        try:
                loop()

        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()
