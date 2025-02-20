import socket

def main():
    #crear un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Definir la dirección y el puerto del servidor
    server_address = ('192.168.183.8', 3000)  # Cambia 'localhost' y 65432 según tu servidor
    try:
        # Conectar al servidor
        client_socket.connect(server_address)
        print("Conectado al servidor en {}:{}".format(*server_address))

        # Enviar un mensaje al servidor
        message = "Hola, servidor!"
        client_socket.sendall(message.encode('utf-8'))
        print("Mensaje enviado: {}".format(message))

        # Esperar la respuesta del servidor
        data = client_socket.recv(1024)
        print("Respuesta del servidor: {}".format(data.decode('utf-8')))

    except Exception as e:
        print("Ocurrió un error: {}".format(e))


if __name__ == "__main__":
    main()
