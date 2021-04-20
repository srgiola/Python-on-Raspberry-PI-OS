import sys
import signal
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import time
from os import system
import RPi.GPIO as GPIO


class Carro:
    def __init__(self, size, contador):
        self.size = size
        self.id = contador
        self.eAgua1 = tiempo = datetime.now()
        self.sAgua1 = None
        self.eShampoo = None
        self.sShampoo = None
        self.eRodillos = None
        self.sRodillos = None
        self.eEscobas = None
        self.sEscobas = None
        self.eAgua2 = None
        self.sAgua2 = None
        self.eRodillos2 = None
        self.sRodillos2 = None

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN) #Este pin es una entrada.
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(3, GPIO.OUT) #Este pin es de salida
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)




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

REF = db.reference("/Registros")
#En Segundos
TIEMPO = 10
AGUA = TIEMPO * 0.15
SHAMPOO = TIEMPO * 0.10
RODILLOS = TIEMPO * 0.20
ESCOBAS = TIEMPO * 0.20


#Size
# 1 - small
# 2 - mid
# 3 - big

while(True):
    CONTADOR = 0
    
    if GPIO.input(2) and (GPIO.input(14) or GPIO.input(15)):
        CONTADOR += 1
        size = 0
        if(GPIO.input(14) == False and GPIO.input(15) == False):
            size = 3
        if(GPIO.input(14) and GPIO.input(15) == False):
            size = 1
        if(GPIO.input(14) == False and GPIO.input(15)):
            size = 2
            
        tiempo = datetime.now()
        GPIO.output(3, True)
        print("Entrada automovil")
        eAgua1 = str(tiempo)
        print(eAgua1 + " Inicio Agua")
        time.sleep(AGUA)
        
        tiempo = datetime.now()
        sAgua1 = str(tiempo)
        print(sAgua1 + "Fin Agua")
        GPIO.output(3, False)
        
        tiempo = datetime.now()
        GPIO.output(4, True)
        eShampoo = str(tiempo)
        print(eShampoo + " Inicio Shampoo")
        time.sleep(SHAMPOO)
        
        tiempo = datetime.now()
        GPIO.output(4, False)
        sShampoo = str(tiempo)
        print(sShampoo + " Salida Shampoo")
        
        tiempo = datetime.now()
        GPIO.output(17, True)
        eRodillos1 = str(tiempo)
        print(eRodillos1 + " Entrada Rodillos")
        time.sleep(RODILLOS)
        
        tiempo = datetime.now()
        GPIO.output(17, False)
        sRodillos1 = str(tiempo)
        print(sRodillos1 + " Salida Rodillos")
        
        tiempo = datetime.now()
        GPIO.output(27, True)
        eEscobas = str(tiempo)
        print(eEscobas + " Entrada Escobas")
        time.sleep(ESCOBAS)
    
        tiempo = datetime.now()
        GPIO.output(27, False)
        sEscobas = str(tiempo)
        print(sEscobas + " Salida Escobas")
        
        tiempo = datetime.now()
        GPIO.output(3, True)
        eAgua2 = str(tiempo)
        print(eAgua2 + " Entrada Agua")
        time.sleep(AGUA)
        
        tiempo = datetime.now()
        GPIO.output(3, False)
        sAgua2 = str(tiempo)
        print(sAgua2 + " Fin Agua")
        
        tiempo = datetime.now()
        GPIO.output(4, True)
        eRodillos2 = str(tiempo)
        print(eRodillos2 + " Entrada Rodillos")
        time.sleep(RODILLOS)
        
        tiempo = datetime.now()
        GPIO.output(4, False)
        sRodillos2 = str(tiempo)
        print(sRodillos2 + " Salida Rodillos")
        print("Salida Automovil")
        
        size2 = ""
        if(size == 1):
            size2 = "Small"
        elif(size == 2):
            size2 = "Mediano"
        elif(size == 3):
            size2 = "Grande"
            
        print("Vehiculo tamano " + size2)
        pago = TIEMPO * 2 * size
        print("Debe Pagar: " + str(size))
        
        REF.push({
            "ID:":CONTADOR,
            "HORA ENTRADA": eAgua1,
            "Entrada Agua 1": eAgua1,
            "Salida Agua 1": sAgua1,
            "Entrada Shampo": eShampoo,
            "Salida Shampo": sShampoo,
            "Entrada Rodillos": eRodillos1,
            "Salida Rodillos": sRodillos1,
            "Entrada Escobas": eEscobas,
            "Salida Escobas": sEscobas,
            "Entrada Agua 2": eAgua2,
            "Salida Agua 2": sAgua2,
            "HORA SALIDA": sAgua2,
            "Tamano": size2,
            })

GPIO.cleanup()