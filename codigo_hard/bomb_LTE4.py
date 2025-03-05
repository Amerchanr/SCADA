import socket
import time
from hcsr04 import HCSR04
from machine import Pin
import dht

# Configuración de sensores
p2 = Pin(25, Pin.IN, Pin.PULL_UP)  # Sensor de flujo
pin_temp = dht.DHT11(Pin(19))      # Sensor de temperatura
distancia1 = HCSR04(5,18)         # Sensor de distancia
rele = Pin(27, Pin.OUT)            # Relé

# Configuración del servidor
HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Esperando conexión...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexión establecida desde {addr}")
    

    try:
        while True:
            # Recibir comando
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            
              

            try:
                comando = int(data)  # Convertir a entero
            except ValueError:
                print(f"Error: Comando no válido recibido ({data})")
                continue  # Ignorar y seguir esperando comandos válidos

            print(f"Comando recibido: {comando}")

            
            pin_temp.measure()
            temperatura = pin_temp.temperature()
            flujo = p2.value()
            ultra1 = distancia1.distance_cm()
            
            
            
            # Control de la bomba
            if (ultra1 < 10) and (flujo == 0) and (temperatura < 28)and(comando==1):
                rele.value(1)  # Activa el relé
                estado_rele = "Encendido"
            else:
                rele.value(0)  # Desactiva el relé
                estado_rele = "Apagado"

                # Enviar datos al cliente
            datos = f"{temperatura},{flujo},{ultra1},{estado_rele}\n"
            conn.sendall(datos.encode())

            print(f"Datos enviados: {datos}")
            time.sleep(3)  # Esperar antes de la siguiente lectura

           
                
                

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()
        print("Cliente desconectado, esperando nueva conexión...")
