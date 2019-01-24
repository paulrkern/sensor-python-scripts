import os
import I2C_LCD_Driver
import RPi.GPIO as GPIO
import time

boom = 60

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

mylcd = I2C_LCD_Driver.lcd()

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def kaboom():
    mylcd.lcd_clear()
    print("You're Dead!")
    os.system('omxplayer temple-bell.mp3 &')
    mylcd.lcd_display_string("You're Dead!",1)
    mylcd.lcd_display_string("Try harder!",2)

while boom > -1:
    time.sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string(str(boom),1)
    boom -=1
    
    if GPIO.input(10) != GPIO.HIGH:
        break

kaboom()     
