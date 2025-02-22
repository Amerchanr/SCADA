# platform: micropython-esp32
# send: wifi
# ip_mpy: 192.168.183.8
# serialport: 
# import usocket as socket
# filename: main.py
import socket

# Agregar nport de donde está el servidor TCP, en el ejemplo: 3000
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
# Cantidad de bytes a recibir
#bufferSize  = 128



sk = socket.socket()
sk.bind(serverAddressPort)
sk.listen(1)
print("Listening on: ", serverAddressPort)


while True:
  conn, addr = sk.accept()
  conn.sendall("ok")
  conn.close()