import tkinter as tk
from tkinter import scrolledtext

# Crear la ventana principal
root = tk.Tk()
root.title("Campo de Texto con Scroll")

# Crear el widget ScrolledText
text_area = scrolledtext.ScrolledText(root, width=40, height=10)
text_area.pack(padx=10, pady=10)

# Insertar texto de ejemplo
text_area.insert(tk.END, "Escribe aquí tu texto...\nPuedes agregar múltiples líneas.\n")

# Iniciar el bucle principal
root.mainloop()