import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo con Canvas")
root.geometry("600x400")  # Tamaño de la ventana

# Crear el Canvas
canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

# Cargar imagen de fondo (usa una imagen PNG en la misma carpeta)
fondo = tk.PhotoImage(file="fondo.png")
canvas.create_image(300, 150, image=fondo)  # Centrar imagen en el Canvas

# Cargar imagen del personaje
personaje = tk.PhotoImage(file="personaje.png")
personaje_id = canvas.create_image(50, 200, image=personaje)  # Posición inicial

# Función para mover el personaje a la derecha con animación
def mover_personaje():
    canvas.move(personaje_id, 5, 0)  # Mueve el personaje 5 píxeles a la derecha
    root.after(50, mover_personaje)  # Llama a la función cada 50ms

# Función para mostrar el texto ingresado en el Canvas
def mostrar_texto():
    mensaje = campo_texto.get()  # Obtener el texto del campo
    canvas.create_text(300, 50, text=mensaje, font=("Arial", 16, "bold"), fill="black")

# Campo de texto
campo_texto = tk.Entry(root, font=("Arial", 14))
campo_texto.pack(pady=5)

# Botón para mostrar texto
boton_texto = tk.Button(root, text="Mostrar Texto", command=mostrar_texto)
boton_texto.pack()

# Botón para iniciar animación
boton_mover = tk.Button(root, text="Mover Personaje", command=mover_personaje)
boton_mover.pack()

# Iniciar la aplicación
root.mainloop()
