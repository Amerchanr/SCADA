import serial
import csv

puerto = "COM6"  # Ajusta el puerto según tu ESP32
baudrate = 115200

ser = serial.Serial(puerto, baudrate, timeout=1)

with open("datos_sensores.csv", "a", newline="") as archivo:
    writer = csv.writer(archivo)
    
    # Escribir encabezados si el archivo está vacío
    if archivo.tell() == 0:
        writer.writerow(["Temperatura", "Flujo", "Nivel"])  
    
    while True:
        linea = ser.readline().decode().strip()
        if linea:
            datos = linea.split(",")  # Separar datos CSV
            print("Recibido:", datos)
            writer.writerow(datos)  # Guardar en el archivo CSV
