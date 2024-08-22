#importamos el tkinter
import tkinter as tk #alias al tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

def abrirVentanaPrincipal():
    
    #Creando un funcion dentro de la funcion
    def funcionSumar():
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        varResult =  num1+num2
        labelTotales.config(text=f"El resultado es: {varResult}")
    
    def funcionMostrarResultado():
        labelRespuesta.config(text=f"Es: {numTarjeta.get()} / {codigo.get()}")
    
    def funcionBorrarTodo():
        messagebox.showinfo("Calculadora","Caja de texto borrado")
        numTarjeta.set("")
        codigo.set("")
        labelTotales.config(text="El resultado es: ")
        labelRespuesta.config(text="Es: ")
        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)
    
    ventana2 = tk.Tk()
    ventana2.title("SISTEMA PRINCIPAL")
    ventana2.geometry("460x460")
    ventana2.resizable(False,False)
    
    #creando las variables
    numTarjeta = tk.StringVar()
    codigo = tk.StringVar()
    
    #Creando la estructura
    label_n_tarjeta = tk.Label(ventana2,text="N° de tarjeta", font=("Arial",15,"bold"))
    label_n_tarjeta.grid(row=0,column=0,padx=60,pady=10)
    
    label_codigo = tk.Label(ventana2,text="Codigo",font=("Arial",15,"bold"))
    label_codigo.grid(row=0,column=1,padx=60,pady=10)
    
    #creando la estructura parte 02
    txtTarjeta = tk.Entry(ventana2, textvariable=numTarjeta,font=("Arial",12,"bold"))
    txtTarjeta.grid(row=1,column=0,padx=10)
    txtTarjeta.config(bg="#fff",font=("Arial",12),fg="red")
    
    txtTarjeta.focus()
    txtCodigo = tk.Entry(ventana2,textvariable=codigo,font=("Arial",12,"bold"))
    txtCodigo.grid(row=1,column=1,padx=10)
    txtCodigo.config(bg="#fff",font=("Arial",12),fg="red",show="*")
    
    
    
    # Crear una línea divisoria horizontal (Separator)
    separator2 = ttk.Separator(ventana2, orient='horizontal')
    separator2.grid(row=2, column=0, columnspan=3, sticky="ew", padx=50, pady=10)
    
    #Creando la estructura parte 03
    label_calcular = tk.Label(ventana2,text="Calcular", font=("Arial",15,"bold"))
    label_calcular.grid(row=3,column=0,padx=0,pady=10)
    entry_num1 = tk.Entry(ventana2, width=10, font=('Arial'),justify='center')
    entry_num1.grid(row=4, column=0, padx=10)
    entry_num2 = tk.Entry(ventana2, width=10, font=('Arial'),justify='center')
    entry_num2.grid(row=5, column=0, padx=10,pady=10)

    ##BOTON DE SUMAR
    boton_sumar = tk.Button(ventana2, text="Sumar + ", fg="white", bg="blue", font=("Arial", 12, "bold"), command=funcionSumar)
    boton_sumar.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

    ##BOTON DE RESTAR
    boton_restar = tk.Button(ventana2, text="Restar -", fg="white", bg="orange", font=("Arial", 12, "bold"))
    boton_restar.grid(row=4, column=1, columnspan=1, padx=15, pady=0)

    ##BOTON DE DIVIDIR
    boton_dividir = tk.Button(ventana2, text="Dividir ÷", fg="white", bg="green", font=("Arial", 12, "bold"))
    boton_dividir.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

    ##BOTON DE MULTIPLICAR
    boton_multiplicar = tk.Button(ventana2, text="Multiplicar x", fg="white", bg="purple", font=("Arial", 12, "bold"))
    boton_multiplicar.grid(row=6, column=1, columnspan=1, padx=5, pady=5)
    
    ################################## INICIO DE LA CREACION DE LOS FRAME ##################################
    # Crear un Frame dentro de la ventana principal
    frame = tk.Frame(ventana2, bg="lightblue", width=300, height=200)
    frame.grid(row=6, column=0, padx=10, pady=10)
    # Añadir widgets al Frame
    labelTotales = tk.Label(frame, text="El resultado es: ")
    labelTotales.grid(row=0, column=0, padx=10, pady=10)
    ################################## FIN DE LA CREACION DE LOS FRAME ##################################
    
    # Crear una línea divisoria horizontal (Separator)
    separator = ttk.Separator(ventana2, orient='horizontal')
    separator.grid(row=10, column=0, columnspan=2, sticky="ew", padx=50, pady=10)
    
        
    #Creado la ultima estructura
    label_resultado = tk.Label(ventana2,text="Mostramos los codigos y la tarjeta", font=("Arial",12,"bold"))
    label_resultado.grid(row=12,column=0,columnspan=2)
    
    ##BOTON DE mostrar
    boton_mostrar = tk.Button(ventana2, text="Mostrar", fg="white", bg="purple", font=("Arial", 12, "bold"), command=funcionMostrarResultado)
    boton_mostrar.grid(row=13, column=0)
    
    # Cargar la imagen
    imagenBotonBorrar = PhotoImage(file="img/borrar2.png")
    """una función anónima (una función lambda) - La función lambda permite definir una función corta sin necesidad de darle un nombre.."""
    boton = tk.Button(ventana2,
                      text="Borrar",
                      compound=tk.LEFT,  # Coloca el texto a la derecha de la imagen
                      font=("Arial", 12, "bold"),
                      image=imagenBotonBorrar, 
                      #command=lambda: print("Botón presionado")
                      command=funcionBorrarTodo)
    boton.grid(row=13, column=1)

    
    labelRespuesta = tk.Label(ventana2, text="Es: ", font=('Arial', 12))
    labelRespuesta.grid(row=14,column=0)
    
    

    
    
    #poner siempre al ultimo, ya que esto permitira que este activo la ventana
    ventana2.mainloop() 
    

#abrirVentanaPrincipal()