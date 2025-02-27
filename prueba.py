import tkinter as tk
import time
import threading

# Variables globales
file_path = "flujo.txt"  # Cambia esto por la ruta de tu archivo
last_line = ""
running = True

def read_file():
    global last_line, running
    while running:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()  # Leer la última línea
                    update_text_area()
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        time.sleep(1)  # Esperar 1 segundo antes de volver a leer

def update_text_area():
    text_area.delete(1.0, tk.END)  # Limpiar el área de texto
    text_area.insert(tk.END, last_line)  # Insertar la última línea

def on_closing():
    global running
    running = False  # Detener el hilo
    root.destroy()  # Cerrar la ventana

# Crear la ventana principal
root = tk.Tk()
root.title("Lectura de Archivo")

text_area = tk.Text(root, height=10, width=50)
text_area.pack()

# Iniciar el hilo para leer el archivo
thread = threading.Thread(target=read_file)
thread.start()

# Asegurarse de que el hilo se detenga al cerrar la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Iniciar el bucle principal de la interfaz
root.mainloop()