import tkinter as tk

def on_button_click():
    print("¡Botón presionado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Botón")

# Crear un botón con tamaño específico
boton = tk.Button(root, text="Presionar", command=on_button_click, width=20, height=2)
boton.pack(pady=20)  # Añadir el botón a la ventana

# Iniciar el bucle principal
root.mainloop()