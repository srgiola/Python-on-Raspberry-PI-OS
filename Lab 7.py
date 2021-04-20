import sys
import signal
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import time
from os import system
import RPi.GPIO as GPIO

PAHT_CRED = '/home/pi/Desktop/cred.json'
URL_DB = 'https://dbarqui2-default-rtdb.firebaseio.com/'
cred = credentials.Certificate(PAHT_CRED)
firebase_admin.initialize_app(cred, {
    'databaseURL': URL_DB
})
REF = db.reference("/")

REF.set({
    'Registros': 
    {
    }
})

estadoAnterior = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(3, GPIO.OUT) # este pin es de salida
GPIO.setup(2, GPIO.IN) #Este pin es una entrada.

REF = db.reference("/Registros")

def insertDB(activida):
    tiempo = datetime.now()
    if(activida == 1):
        GPIO.output(3, False)
        print("Se ha detectado una interrupcion de sensor a las", str(tiempo))
        REF.push({        
                    "Fecha y hora": tiempo.strftime("%m/%d/%Y, %H:%M:%S"),
                    "Accion": "Interrupcion",     
                    })
        
    elif(activida == 0):
        GPIO.output(3, True)
        print("Se ha detectado una continuidad de sensor a las", str(tiempo))
        REF.push({        
                    "Fecha y hora": tiempo.strftime("%m/%d/%Y, %H:%M:%S"),
                    "Accion": "Continuidad",     
                    })
        
while True:
    tiempo = datetime.now()
    if GPIO.input(2) and estadoAnterior == 0:
        insertDB(1)
        estadoAnterior = 1
    elif not(GPIO.input(2)) and estadoAnterior == 1:
        insertDB(0)
        estadoAnterior = 0
GPIO.cleanup()
