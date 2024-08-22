import tkinter as kin 
from tkinter import messagebox
from modulos.principal import *

ventana = kin.Tk()
ventana.title("Login")
ventana.geometry("350x450")
ventana.resizable(False,False)

def validacion():
    messagebox.showinfo("mensaje","Esto es un mensaje mio")

    if usuario.get() == "luis" and password.get() == "juan":
        messagebox.showinfo("mensaje","El usuario y la contraseña son corectas")
        ventana.destroy()
        abrirVentanaPrincipal()
    else:
        messagebox.showerror("mensaje","El usuario y la contraseña son incorectas")
    
    
    

    
#creando variable usuario
usuario = kin.StringVar()
password = kin.StringVar()



titulo = kin.Label(ventana,text="INICIAR SESION", font=("Arial",12,"bold"))
titulo.grid(row=0,column=0,columnspan=2)
# Usuario 
lblUser = kin.Label(ventana,text="Usuario",font=("Arial",10,"bold"))
lblUser.grid(row=1,column=0,padx=80,pady=4,sticky="w")

txtUser = kin.Entry(ventana,font=("arial",12),textvariable=usuario)
txtUser.grid(row=2,column=0,padx=80,pady=10)
# Password 
lblPassword = kin.Label(ventana,text="Contraseña",font=("Arial",10,"bold"))
lblPassword.grid(row=3,column=0,padx=80,pady=4,sticky="w")

txtPassword = kin.Entry(ventana,font=("arial",12),textvariable=password)
txtPassword.grid(row=4,column=0,padx=80,pady=10)

# Enviar 
button_1 = kin.Button(ventana, text="Ingresar", width=10, command=validacion)
button_1.grid(row=5,column=0,padx=10,pady=6,columnspan=2)

ventana.mainloop()