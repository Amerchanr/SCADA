import tkinter as tk
from tkinter import Tk, Frame
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import font
import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate("final\\personas.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://usuarios-47379-default-rtdb.firebaseio.com/"})

##crear una ventana principal
ventana = tk.Tk()
ventana.title("ventana inicio")
##definir tamaño de la ventana a tamaño completo
ventana.attributes('-fullscreen',1)
##definir el color del fondo de la ventana
ventana.config(bg='white')
#"definir la fuente para botones y titulo"
fuentebotones=font.Font(family="Arcade Classic", size=30, weight="bold")
fuentetitulo=font.Font(family="Arcade Classic", size=75, weight="bold")
fuentebotonesventanas=font.Font(family="Arcade Classic", size=15, weight="bold")
fuentetitbrick=font.Font(family="Arcade Classic", size=125, weight="bold")
fuenteusucontra=font.Font(family="Arcade Classic", size=55, weight="bold")
fuentescada=font.Font(family="Arcade Classic", size=20,weight="bold")

#configuracion de listas para para las graficas
eje_x_grafica_temp = []
for i in range(0,101,5):
    eje_x_grafica_temp.append(i) # eje x

eje_y_grafica_temp = [None,None,None,None,None] #eje y 
for i in range((len(eje_x_grafica_temp)-len(eje_y_grafica_temp))):
    eje_y_grafica_temp.append(None)
    
eje_x_grafica_flujo = []
for i in range(0,101,5):
    eje_x_grafica_flujo.append(i) # eje x

eje_y_grafica_flujo = [None,None,None,None,None] #eje y 
for i in range((len(eje_x_grafica_flujo)-len(eje_y_grafica_flujo))):
    eje_y_grafica_flujo.append(None)

# Variables globales para widgets de entrada
caja_texto_usuario = None
caja_texto_contraseña = None
text_area = None




def Scada():
    """Abre la ventana SCADA después del registro."""
    ventana_SCADA = tk.Toplevel(ventana)
    ventana_SCADA.attributes('-fullscreen', 1)
    ventana_SCADA.config(bg='white')
    
    # Crear el Canvas
    canvas_botones = tk.Canvas(ventana_SCADA, width=300, height=800, bg="white")
    canvas_botones.place(x=975,y=0)
    canvas_animacion =tk.Canvas(ventana_SCADA,width=600,height=400,bg='lightblue') 
    canvas_animacion.place(x=0,y=0)
    canvas_camptext =tk.Canvas(ventana_SCADA,width=368,height=400,bg='white') 
    canvas_camptext.place(x=602,y=0)
    canvas_graficas =tk.Canvas(ventana_SCADA,width=970,height=400,bg='lightblue') 
    canvas_graficas.place(x=0,y=400)

    #Botones Scada
    boton_volver=tk.Button(ventana_SCADA,text='volver',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=ventana_SCADA.destroy,width=16)
    canvas_botones.create_window(150,75,window=boton_volver)
    boton_historico=tk.Button(ventana_SCADA,text='Historico',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=ventana_SCADA.destroy,width=16)
    canvas_botones.create_window(150,200,window=boton_historico)
    boton_Parar=tk.Button(ventana_SCADA,text='Parar Bomba',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=ventana_SCADA.destroy,width=16)
    canvas_botones.create_window(150,300,window=boton_Parar)
    boton_Start=tk.Button(ventana_SCADA,text='Bomba Start',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=ventana_SCADA.destroy,width=16)
    canvas_botones.create_window(150,400,window=boton_Start)
    boton_PaSistem=tk.Button(ventana_SCADA,text='Parar Sistema',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=ventana_SCADA.destroy,width=16)
    canvas_botones.create_window(150,525,window=boton_PaSistem)
    boton_ReiSistema=tk.Button(ventana_SCADA,text='Reinicio de Sistema',font=(fuentescada),bg='#000000',fg='white',relief='raised',command=ventana_SCADA.destroy,width=16)
    canvas_botones.create_window(150,650,window=boton_ReiSistema)
    
    #widgets camp text
    Titulo_advertencia = tk.Label(ventana_SCADA,text='¡Advertencias!',font=(fuentescada,40),bg='white',fg='red',)
    canvas_camptext.create_window(200,50,window=Titulo_advertencia)
    Advertencia = tk.Label(ventana_SCADA,text='aqui se presentaran las\nadvertencias presentadas por el \nsistema',font=(fuentescada,15),bg='white',fg='black',)
    canvas_camptext.create_window(200,150,window=Advertencia)
    Advertencia_2 = tk.Label(ventana_SCADA,font=(fuentescada,15),bg='white',fg='black',text='soy la prueba de que existo')
    canvas_camptext.create_window(200,250,window=Advertencia_2)

    #graficas
    frame_temperatura = Frame(canvas_graficas,  bg='blue',pady=20,padx=20)
    frame_temperatura.grid(column=0,row=0, sticky='nsew')
    def cambios_de_valores_temperatura():
        if None in eje_y_grafica_temp:
            eje_y_grafica_temp.remove(None)
            eje_y_grafica_temp.append(random.randrange(0,101,1))
        else:
            eje_y_grafica_temp.pop(0)
            eje_y_grafica_temp.append(random.randrange(0,101,1))
        fig, axs = plt.subplots( dpi=80, figsize=(5,5), 
	    sharey=True, facecolor='#00f9f844')
        fig.suptitle('Grafica de Temperatura')
        axs.plot(eje_x_grafica_temp, eje_y_grafica_temp, color = 'm')
        canvas = FigureCanvasTkAgg(fig, master = frame_temperatura)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0)
        ventana.after(1000,cambios_de_valores_temperatura)
    frame_temperatura.after(100,cambios_de_valores_temperatura)
    
    frame_flujo = Frame(canvas_graficas,  bg='blue',pady=20,padx=20)
    frame_flujo.grid(column=1,row=0, sticky='nsew')
    def cambios_de_valores_flujo():
        if None in eje_y_grafica_flujo:
            eje_y_grafica_flujo.remove(None)
            eje_y_grafica_flujo.append(random.randrange(0,2))
        else:
            eje_y_grafica_flujo.pop(0)
            eje_y_grafica_flujo.append(random.randrange(0,2))
        fig, axs = plt.subplots( dpi=80, figsize=(5,5), 
        sharey=True, facecolor='#00f9f844')
        fig.suptitle('Grafica de Flujo')
        axs.plot(eje_x_grafica_flujo, eje_y_grafica_flujo, color = 'm')
        canvas = FigureCanvasTkAgg(fig, master = frame_flujo)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=0)
        ventana.after(1000,cambios_de_valores_flujo)
    frame_flujo.after(100,cambios_de_valores_flujo)
#advertencias
    def advertencia_de_temperatura():
        if eje_y_grafica_temp[-1] >50:
            Advertencia_2.config(text='¡¡¡ADVETENCIA!!!\n La temperatura  actual\nsobrepasa la temperatura\noptima',fg='red')
        else:
            Advertencia_2.config(text='')
        ventana.after(100,advertencia_de_temperatura)
    ventana.after(100,advertencia_de_temperatura)
    def advertencia_de_flujo():
        if (eje_y_grafica_flujo[-1]) == 0 and (eje_y_grafica_flujo[-2] == 0) and (eje_y_grafica_flujo[-3]) == 0 :
            Advertencia.config(text='¡¡¡ADVETENCIA!!!\n El flujo de agua actual\nes menor al flujo\noptimo recomendado',fg='red')
        else:
            Advertencia.config(text='aqui se presentaran las\nadvertencias presentadas por el \nsistema',font=(fuentescada,15),bg='white',fg='black')
        ventana.after(100,advertencia_de_flujo)
    ventana.after(100,advertencia_de_flujo)


#funcion ventana de registro 

def registro():
    ventana_registro=tk.Toplevel(ventana)
    ventana_registro.attributes('-fullscreen',1)
    ventana_registro.config(bg='white')
    registrar= tk.Label(ventana_registro,text='registro',font=(fuentetitbrick),bg='white',fg='black')
    registrar.place(x=300,y=0)
    boton_volver=tk.Button(ventana_registro,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_registro.destroy)
    boton_volver.place(x=1180,y=20) 
    usuario=tk.Label(ventana_registro,text='usuario',font=(fuenteusucontra),bg='white',fg='black')
    usuario.place(x=500,y=200)
    caja_texto_usuario = tk.Text(ventana_registro, height=1, width=40)
    caja_texto_usuario.place(x=475,y=290)
    contraseña=tk.Label(ventana_registro,text='contraseña',font=(fuenteusucontra),bg='white',fg='black')
    contraseña.place(x=450,y=330)
    caja_texto_contraseña = tk.Text(ventana_registro, height=1, width=40)
    caja_texto_contraseña.place(x=475,y=425)
    text_area = tk.Text(ventana_registro,height=3,width=50)
    text_area.place(x=500,y=480)
        
    def dataregist():
        texto_usuario=caja_texto_usuario.get("1.0", tk.END).strip()
        texto_contraseña=caja_texto_contraseña.get("1.0", tk.END).strip()
        referencia= db.reference(f'usuarios/{texto_usuario}')
        name=caja_texto_usuario.get("1.0", tk.END).strip()
        if referencia.get():
                text_area.delete("1.0", tk.END) 
                text_area.insert(tk.END,f'El Usuario {name}, ya se encuentra registrado')
        else:        
            text_area.delete("1.0", tk.END)    
            referencia.set({'contraseña':texto_contraseña})
            def destruir_regist():
                 ventana_registro.destroy
            text_area.insert(tk.END,f'Hola {name}, Bienvenido desde la siguiente pestaña podrá observar lo referente a su sistema de alcantalillado')
            ventana_registro.after(100000,destruir_regist)
            Scada()
                      
    boton_registro=tk.Button(ventana_registro,text='registrarse',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=dataregist)
    boton_registro.place(x=500,y=600)

def inicio_sesion():
    ventana_inicio=tk.Toplevel(ventana)
    ventana_inicio.attributes('-fullscreen',1)
    ventana_inicio.config(bg='white')
    iniciar= tk.Label(ventana_inicio,text='inicie sesión',font=(fuentetitbrick),bg='white',fg='black')
    iniciar.place(x=200,y=20)
    boton_volver=tk.Button(ventana_inicio,text='volver',font=(fuentebotonesventanas),bg='#000000',fg='white',relief='raised',command=ventana_inicio.destroy)
    boton_volver.place(x=1180,y=20)
    usuario=tk.Label(ventana_inicio,text='usuario',font=(fuenteusucontra),bg='white',fg='black')
    usuario.place(x=500,y=220)
    caja_texto_usuario = tk.Text(ventana_inicio, height=1, width=40)
    caja_texto_usuario.place(x=475,y=310)
    contraseña=tk.Label(ventana_inicio,text='contraseña',font=(fuenteusucontra),bg='white',fg='black')
    contraseña.place(x=450,y=350)
    caja_texto_contraseña = tk.Text(ventana_inicio, height=1, width=40)
    caja_texto_contraseña.place(x=475,y=425)
    
    text_area = tk.Text(ventana_inicio,height=3,width=50)
    text_area.place(x=500,y=450)    
    def inicio():
        texto_usuario=caja_texto_usuario.get("1.0", tk.END).strip()
        texto_contraseña=caja_texto_contraseña.get("1.0", tk.END).strip()
        referencia= db.reference(f'usuarios/{texto_usuario}')
        name=caja_texto_usuario.get("1.0", tk.END).strip()
        dato_usuario=referencia.get()
        contr_usua=dato_usuario.get('contraseña')
        print(contr_usua)
        print(texto_contraseña)
        if (contr_usua== texto_contraseña):

             text_area.insert(tk.END,f'Hola {name}, Bienvenido desde la siguiente pestaña podrá observar lo referente a su sistema de alcantalillado')
             def destruir_inicio():
                  ventana_inicio.destroy
             #ventana_inicio.after(5000,destruir_inicio)
             #ventana_inicio.destroy
             #destruir_inicio()
             Scada()
        else:
             text_area.insert(tk.END,f'Hola {name}, el usuario o la contraseñaa estan incorrectos')
    boton_sesion=tk.Button(ventana_inicio,text='iniciar sesion',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=inicio)
    boton_sesion.place(x=500,y=550)    


titulo = tk.Label(ventana,text='SCADA SISTEMA INTERNO\nDE ALCANTARILLADO',font=(fuentetitulo),bg='white',fg='black')
titulo.place(x=0,y=40)
registrarse= tk.Button(ventana,text='registrarse',font=fuentebotones,bg='#000000',fg='white',relief='raised',command=registro)
registrarse.place(x=530,y=350)
but_inicio= tk.Button(text='Inicio de Sesión',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=inicio_sesion)
but_inicio.place(x=480,y=440)
#brick_Breaker= tk.Button(text='Brick Breacker',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=crear_ventana_brick)
#brick_Breaker.place(x=490,y=530)
salir= tk.Button(text='Salir',font=(fuentebotones),bg='#000000',fg='white',relief='raised',command=ventana.quit)
salir.place(x=600,y=620)
ventana.mainloop()  
