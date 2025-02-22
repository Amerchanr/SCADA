# platform: micropython-esp32
# send: wifi
# ip_mpy: 192.168.4.1
# serialport:
# filename: stempt.py


from machine import Pin               # importa la clase Pin del módulo machine
import dht                            # importa el módulo dht
  
pin_04 = dht.DHT22(Pin(15))            # crea el objeto pin_04 para un módulo DHT22 en el pin GPIO 04
  
pin_04.measure()                      # realiza la lectura de la temperatura y humedad
temperatura = pin_04.temperature()    # asigna a la variable "temperatura" la temperatura 
print ("La temperatura es de " + str(temperatura) + "ºC ")