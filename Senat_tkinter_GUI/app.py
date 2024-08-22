#Importamos el TKINTER
import tkinter as tk
#Importamos los messageBox
from tkinter import messagebox
#Importamos el modulo del archivo principal y usar todo*
# from modulos.principal import *

#Creamos una funcion para mostrar mensajes
def mensajeInfo():
    messagebox.showinfo("Mensaje","Esto es un mensaje de INFO")
    
def mensajeError():
    messagebox.showerror("Mensaje","ERROR, tenemos un problema!")
    
def mensajeAdvertencia():
    messagebox.showwarning(title="Mensaje", message="Advertencia!!!")
    # ventana.destroy()
    # abrirVentanaPrincipal()
    
#Inicializamos la clase TK()
ventana = tk.Tk() 
#Menciono el nombre de la ventana
ventana.title("APLICACION DE MENSAJES")
#Icono en la ventana
ventana.iconbitmap("icons/favicon.ico")
#Tamaño de la ventana
ventana.geometry("350x450")
#Color del fondo de la ventana
ventana.config(bg="#0859aa")
#Transparencia a la ventana
ventana.wm_attributes("-alpha",0.8)
#El usuario no permite modificar la ventana
ventana.resizable(False,False)

#AGREGANDO BOTONES
boton1 = tk.Button(ventana, text="Info", width=10,height=5,command=mensajeInfo)
boton1.grid(row=0,column=0,padx=50,pady=30)

boton2 = tk.Button(ventana, text="Error", width=10,height=5,command=mensajeError) 
boton2.grid(row=0,column=1,padx=50,pady=30)

boton3 = tk.Button(ventana, text="B3", width=10,height=5,command=mensajeAdvertencia)
boton3.grid(row=1,column=0,padx=50,pady=30)

boton4 = tk.Button(ventana, text="B4", width=10,height=5)
boton4.grid(row=1,column=1,padx=50,pady=30)


#Mantener la ventana abierta
ventana.mainloop() 