# platform: micropython-esp32
# send: wifi
# ip_mpy: 192.168.4.1
# serialport: 
# filename: Sensor_Flujo.py

from machine import Pin

# create an input pin on pin #2, with a pull up resistor
p2 = Pin(26, Pin.IN, Pin.PULL_UP)

# read and print the pin value
print(p2.value())
