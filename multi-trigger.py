import os
import I2C_LCD_Driver
import RPi.GPIO as GPIO
import time

mylcd = I2C_LCD_Driver.lcd()
TiltPin = 23 # Physical pin for tilt sensor
PressurePin = 10 # Physical pin for pressure button

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PressurePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setwarnings(False)
    countdown()

def countdown():
    boom = 60
    while boom > -1:
        time.sleep(1)
        mylcd.lcd_clear()
        mylcd.lcd_display_string(str(boom),1)
        boom -=1
    kaboom()

def kaboom():
    mylcd.lcd_clear()
    print("You're Dead!")
    mylcd.lcd_display_string("You're Dead!",1)
    mylcd.lcd_display_string("Try harder!",2)

def loop():
    GPIO.add_event_detect(TiltPin, GPIO.FALLING, callback=kaboom, bouncetime=100)
    GPIO.add_event_detect(PressurePin, GPIO.HIGH, callback=kaboom)

def destroy():
    print("#####################################")
    print("#           CTRL+C DETECTED          ")
    print("#####################################")
    GPIO.cleanup() # Release resource

if __name__ == '__main__':      # Program start from here
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        destroy()
