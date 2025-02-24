# platform: micropython-esp32
# send: wifi
# ip_mpy: 192.168.183.8
# serialport: 
# import usocket as socket
# filename: test_ultra.py
#import stempt
from hcsr04 import HCSR04
from time import sleep
from machine import Pin               # importa la clase Pin del módulo machine

#sintax=(trig, echo)

distancia1 = HCSR04(5, 18)
distancia2= HCSR04(4, 19)
distancia3 = HCSR04(21, 23)
distancia4 = HCSR04(12, 22)
while True:

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