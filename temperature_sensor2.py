import sys
import Adafruit_DHT as sensor
import time
import datetime

while True:
	humidity, temperature = sensor.read_retry(11,4)
	time.sleep(10)
	print datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S")
	print 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity)

