#!/usr/bin/python
import sys
sys.path.append('/home/pi/Desktop/lcd')
import lcd
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()


GPIO.setmode(GPIO.BCM)
lcd.lcd_init()
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("temperature(C):", 2)

gtemp = 0

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)#switch input


GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
button = GPIO.input(27)
#check = 0

def my_callback(channel):
  try:
    if(GPIO.input(17)):
        
        format_float = "{:.2f}".format(gtemp)
        if GPIO.input(27):
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string( "", 2)            
            #print ("release")  
        else:
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string( format_float, 2) 
            #print ("press")
  except:
       print("s")
    

GPIO.add_event_detect(27, GPIO.BOTH, callback=my_callback) 

while True:
  try:
    while  (GPIO.input(17)): #switch is on, read temp every 1s
        gtemp = sensor.get_temperature()
        format_float = "{:.2f}".format(gtemp)
        print("The temperature is %s celsius" % gtemp)
        #if check == 1:
            #lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            #lcd.lcd_string( "", 2)
            #check = 0
        time.sleep(1)
  
  except:
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string( "Error", 2)       
    #check = 1
  if(GPIO.input(17) == 0):
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string( "", 2)
  








    
