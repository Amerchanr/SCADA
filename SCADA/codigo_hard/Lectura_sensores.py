from hcsr04 import HCSR04
from time import sleep
from machine import Pin               # importa la clase Pin del módulo machine
import dht
import machine
import time
#sensor de flujo
# create an input pin on pin #2, with a pull up resistor(Flujo)
p2 = Pin(17, Pin.IN, Pin.PULL_UP)

pin_temp = dht.DHT11(Pin(19))            # crea el objeto pin_04 para un módulo DHT22 en el pin GPIO 04


# Definir el pin del relé (cambia el número según tu conexión)
rele = machine.Pin(16, machine.Pin.OUT)



#sintax=(trig, echo)

distancia1 = HCSR04(5, 18)

while True:
    sleep(3)
    pin_temp.measure()                      # realiza la lectura de la temperatura y humedad
    temperatura = pin_temp.temperature()    # asigna a la variable "temperatura" la temperatura
    print("La temperatura es de " + str(temperatura) + "ºC" )
    sleep(2)
    # read and print the pin value sensor flujo
    print(f'sensor flujo{p2.value()}')
    sleep(2)
    ultra1=distancia1.distance_cm()  
    print ("La distancia promedio es de " + str(ultra1))
    if (ultra1<10)and (p2.value()==1)and(temperatura<26):
        print("Encendiendo relé")
        rele.value(1)  # Activa el relé
        time.sleep(2)  # Espera 2 segundos
        print("Apagando relé")
    if (ultra1>10)or (p2.value()==0)or(temperatura>26): 
        rele.value(0)  # Desactiva el relé
        time.sleep(2) 