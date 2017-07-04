import CHIP_IO.GPIO as GPIO
from time import sleep


ledPin = "CSID3"

GPIO.setup(ledPin, GPIO.OUT)

try:
	while True:
		GPIO.output(ledPin, True)
		sleep(1)
		GPIO.output(ledPin, False)
		sleep(1)
	
#exit with CTRL+C			
except KeyboardInterrupt:
	print("exiting")
	
#unexport GPIOs upon exiting      
finally:
	GPIO.cleanup() 
