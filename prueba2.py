import tkinter as tk
from tkinter import PhotoImage

def on_button_click():
    print("¡Botón presionado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Canvas")

# Crear un canvas
canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
canvas.pack()

# Agregar un botón al canvas
button = tk.Button(root, text="Presionar", command=on_button_click)
canvas.create_window(200, 50, window=button)  # Posición (x, y)

# Agregar un campo de texto al canvas
entry = tk.Entry(root)
canvas.create_window(200, 100, window=entry)  # Posición (x, y)

# Cargar una imagen (asegúrate de tener una imagen en el mismo directorio)
# Puedes usar .png o .gif, ya que tkinter no soporta .jpg directamente
try:
    image = PhotoImage(file="imagen.png")  # Cambia "imagen.png" por el nombre de tu imagen
    canvas.create_image(200, 200, image=image)  # Posición (x, y)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")

# Iniciar el bucle principal
root.mainloop()