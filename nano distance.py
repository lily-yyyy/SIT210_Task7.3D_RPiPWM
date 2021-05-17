import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG=24
ECHO=23
LED=21

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
	GPIO.output(TRIG, False)
	print("waiting for sensor to settle")
	time.sleep(2)

	GPIO.output(TRIG, False)
	time.sleep(0.1)
	GPIO.output(TRIG, True)
	
	while GPIO.input(ECHO)==0:
		pulse_start=time.time()

	while GPIO.input(ECHO)==1:
		pulse_start=time.time()

	pulse_duration=pulse_end_pulse_start

	distance = pulse_duration * 17150
	distance = round(distance,2)
	print(distance)
	if distance>30:
	   GPIO.output(LED,GPIO.LOW)
	else:
	   GPIO.output(LED,GPIO.HIGH)