import sys
import Adafruit_DHT as sensor

while True:
	humidity, temperature = sensor.read_retry(11,4)
	
	print 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity)
