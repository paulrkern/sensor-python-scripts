import I2C_LCD_Driver
from time import *

mylcd = I2C_LCD_Driver.lcd()

mylcd.lcd_display_string("Paul Rocks!",1)
