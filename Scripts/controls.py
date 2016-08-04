# Home_Weather_Display.py
#
# This is an project for using the Grove RGB LCD Display and the Grove DHT Sensor from the GrovePi starter kit
# 
# In this project, the Temperature and humidity from the DHT sensor is printed on the RGB-LCD Display
#
#
# Note the dht_sensor_type below may need to be changed depending on which DHT sensor you have:
#  0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
#  1 - DHT22 - white one, aka DHT Pro or AM2302
#  2 - DHT21 - black one, aka AM2301
#
# For more info please see: http://www.dexterindustries.com/topic/537-6c-displayed-in-home-weather-project/
#
'''
The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time
import datetime
import decimal
from grovepi import *
from grove_rgb_lcd import *

dht_sensor_port = 7		# Connect the DHt sensor to port 7
dht_sensor_type = 0             # change this depending on your sensor type - see header comment

daglamp = 4
warmtelamp = 3
pinMode(daglamp,"OUTPUT")
pinMode(warmtelamp,"OUTPUT")

# Function Definitions

setRGB(0,128,64)
setRGB(0,128,0)	
setText("  Hallo Jack!")

while True:
	try:
		now = datetime.datetime.now()
		localtime = time.asctime( time.localtime(time.time()) )
		tijd = str(localtime)
		tijd1 = now.strftime("%H:%M")
		datum = now.strftime("%Y-%m-%d")

		print(tijd)
		print tijd1
		#setText("     "+tijd1)
		i = 0
		t = 0
		h = 0
		while i < 10:
			[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
			t = t + temp
			h = h + hum
				#print(i)
			i = i + 1
				#print("temp =", temp, "C\thumidity =", hum,"%", i, t, h)
				#print("Average Temp:", t//i)
		
		digitalWrite(daglamp,1)
		 	
		
		tt=str(t/10)
		hh=str(h/10)	

		setRGB(0,128,64)
		if t//10 < 21:
			setRGB(0,102,255)
			digitalWrite(warmtelamp,1)
		elif t//10 > 25:
			setRGB(255,102,0)
			digitalWrite(warmtelamp,0)
		else:
			setRGB(0,200,0)

		#setText("Temp:" + tt + "C      " + "Humidity :" + hh + "%")
		setText("     "+tijd1+"      "+ tt + "C      " + hh + "%")

	except KeyboardInterrupt:	# Turn lights off before stopping
		time.sleep(.2)
		digitalWrite(warmtelamp,0)
		time.sleep(.2)
		digitalWrite(daglamp,0)
		setRGB(0,0,0)
		setRGB(0,0,0)
        	break			
	except (IOError,TypeError) as e:
		print("Error")
