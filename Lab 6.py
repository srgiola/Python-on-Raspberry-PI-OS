from datetime import datetime
import time
from os import system
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(3, GPIO.OUT) # este pin es de salida
GPIO.setup(2, GPIO.IN) #Este pin es una entrada.

estadoAnterior = 0

while True:
    tiempo = datetime.now()
    if GPIO.input(2) and estadoAnterior == 0:
        GPIO.output(3, False)
        print("Se ha detectado una interrupcion de sensor a las", str(tiempo))
        estadoAnterior = 1
    elif not(GPIO.input(2)) and estadoAnterior == 1:
        GPIO.output(3, True)
        print("Se ha detectado una continuidad de sensor a las", str(tiempo))
        estadoAnterior = 0
GPIO.cleanup()
