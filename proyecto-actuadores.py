from machine import Pin
import time

IN1 = Pin(13, Pin.OUT)
IN2 = Pin(14, Pin.OUT)
EN_A = Pin(15, Pin.OUT)
b_subir = Pin(12, Pin.OUT)
b_bajar = Pin(11, Pin.OUT)
b_paro = Pin(10, Pin.OUT)

EN_A.high()

def subir():
    IN1.high()
    IN2.low()

def bajar():
    IN1.low()
    IN2.high()

def paro():
    IN1.low()
    IN2.low()

while True:

    if b_subir.value() == 1:
        subir()
        print("Subiendo")
        time.sleep(1)
    if b_bajar.value() == 1:
        bajar()
        print("Bajando")
        time.sleep(1)
    if b_paro.value() == 1:
        paro()
        print("Detenido")
        time.sleep(1)
    