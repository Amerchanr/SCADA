# platform: micropython-esp32
# send: wifi
# ip_mpy: 192.168.183.8
# serialport: 
# import usocket as socket
# filename: main.py
#import stempt
from hcsr04 import HCSR04
from time import sleep
from machine import Pin               # importa la clase Pin del módulo machine
import dht                            # importa el módulo dht
import socket


# Agregar nport de donde está el servidor TCP, en el ejemplo: 3000
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]



sk = socket.socket()
sk.bind(serverAddressPort)
sk.listen(1)
print("Listening on: ", serverAddressPort)





# create an input pin on pin #2, with a pull up resistor
p2 = Pin(26, Pin.IN, Pin.PULL_UP)

pin_04 = dht.DHT11(Pin(13))            # crea el objeto pin_04 para un módulo DHT22 en el pin GPIO 04


#sintax=(trig, echo)

distancia1 = HCSR04(5, 18)
distancia2= HCSR04(4, 19)
distancia3 = HCSR04(21, 23)
distancia4 = HCSR04(12, 22)
while True:
  conn, addr = sk.accept()
  conn.sendall("ok")
  sleep(3)
  pin_04.measure()                      # realiza la lectura de la temperatura y humedad
  temperatura = pin_04.temperature()    # asigna a la variable "temperatura" la temperatura 
  conn.sendall("La temperatura es de " + str(temperatura) + "ºC" )
  conn.sendall("La temperatura es de " + str(temperatura) + "ºC ")
  sleep(2)

  # read and print the pin value sensor flujo
  conn.sendall(f'sensor flujo{p2.value()}')

  print(f'sensor flujo{p2.value()}')

  sleep(2)
  ultra1=distancia1.distance_cm()
  sleep(2)
  ultra2=distancia2.distance_cm()
  sleep(2)
  ultra3=distancia3.distance_cm()
  sleep(2)
  ultra4=distancia4.distance_cm()
  promedio=((ultra1+ultra2+ultra3+ultra4)/4)
  print(f'ultra1 {ultra1}')
  print(f'ultra2 {ultra2}')
  print(f'ultra3 {ultra3}')
  print(f'ultra4 {ultra4}')
  print(promedio)
  print ("La distancia promedio es de " + str(promedio))
