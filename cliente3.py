import socket

# Configuración del cliente
ESP32_IP = "192.168.206.8"  # Dirección IP del ESP32
PORT = 12345

# Conectar con el servidor (ESP32)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ESP32_IP, PORT))

print("Conectado al ESP32")

try:
    while True:
        # Recibir datos
        data = client_socket.recv(1024).decode().strip()
        
        if not data:
            break

        print(f"Datos recibidos: {data}")

        # Separar los valores
        valores = data.split(",")
        if len(valores) == 4:
            temperatura, flujo, nivel, estado_rele = valores

            # Guardar en archivos TXT
            with open("temperatura.txt", "a") as temp_file:
                temp_file.write(f"{temperatura}\n")

            with open("flujo.txt", "a") as flujo_file:
                flujo_file.write(f"{flujo}\n")

            with open("nivel.txt", "a") as nivel_file:
                nivel_file.write(f"{nivel}\n")

            with open("estado_bomba.txt", "a") as estado_file:
                estado_file.write(f"{estado_rele}\n")

except KeyboardInterrupt:
    print("Conexión cerrada por el usuario.")

finally:
    client_socket.close()
