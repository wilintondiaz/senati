import tkinter as kin 
from tkinter import ttk
from tkinter import messagebox
from modulos.ejercicio_1 import *
from modulos.ejercicio_2 import *
from modulos.ejercicio_3 import *
from modulos.ejercicio_4 import *
from modulos.ejercicio_5 import *
from modulos.ejercicio_6 import *
from modulos.ejercicio_7 import *
from modulos.ejercicio_8 import *
def abrirVentanaPrincipal():
    
    def functionEjercicio01():
        messagebox.showerror("Mensaje","Yendo al ejercicio 01")
        abrirventanaEjercicio_1()
    
    ventana2 = kin.Tk()
    ventana2.title("SISTEMAPRINCIPAL") 
    ventana2.geometry("350x450")
    ventana2.resizable(False,False) 

    button_1 = kin.Button(ventana2, text="Ejercicio 01", width=20,command=functionEjercicio01)
    button_1.grid(row=0,column=0,padx=12,pady=10)
    
    button_2 = kin.Button(ventana2, text="ejercicio 02", width=20)
    button_2.grid(row=0,column=1,padx=12,pady=10)
    
    button_3 = kin.Button(ventana2, text="Ejercicio 03", width=20)
    button_3.grid(row=1,column=0,padx=12,pady=10)
    
    button_4 = kin.Button(ventana2, text="ejercicio 04", width=20)
    button_4.grid(row=1,column=1,padx=12,pady=10)
    
    button_5 = kin.Button(ventana2, text="Ejercicio 05", width=20)
    button_5.grid(row=2,column=0,padx=12,pady=10)
    
    button_6 = kin.Button(ventana2, text="ejercicio 06", width=20)
    button_6.grid(row=2,column=1,padx=12,pady=10)
    
    button_7 = kin.Button(ventana2, text="Ejercicio 07", width=20)
    button_7.grid(row=3,column=0,padx=12,pady=10)
    
    button_8 = kin.Button(ventana2, text="ejercicio 08", width=20)
    button_8.grid(row=3,column=1,padx=12,pady=10)
    
    ventana2.mainloop()
    
# abrirVentanaPrincipal()