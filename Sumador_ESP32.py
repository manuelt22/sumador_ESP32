import tkinter as GUI
from tkinter import ttk
import serial
import time

# Configuración de la ventana
ventana = GUI.Tk()
ventana.title('Conexión ESP32')
ventana.geometry('300x300')
ventana.configure(bg="tan")

# Pestaña
notebook = ttk.Notebook(ventana)
notebook.pack(pady=2, expand=True)
frame1 = GUI.Frame(notebook, width=400, height=280, bg="Lightblue")
frame1.pack(fill='both', expand=True)
notebook.add(frame1, text='Sumador')

# Configuración del puerto serie
PUERTO = "COM3"
arduino = serial.Serial(port=PUERTO, baudrate=115200, timeout=.1)

# Función conectar
def CONECTAR():
    global PUERTO
    print("función conectar")
    PUERTO = EntryCOM.get()
    EntryCOM.config(state="readonly")  
    LabelCOM_NAME.pack_forget()  
    BotonCONECT.pack_forget()  
    campos.pack(padx=1, pady=2)  

# Función enviar datos
def SEND():
    print("función ENVÍO DE DATOS")
    x = SpinDATA.get()
    arduino.write(bytes(x + '\n', 'utf-8'))  
    time.sleep(0.1)  
    data = arduino.readline().decode('utf-8').strip()  

    # Mostrar los datos recibidos
    LabelRECIVE.config(text="dato recibido: " + data)

# Función cerrar
def CERRAR():
    print("cerrar")
    arduino.close()
    ventana.destroy()

# Función para cambiar puerto y resetear valores
def cambio():
    EntryCOM.config(state="normal")  
    campos.pack_forget()  
    BotonCONECT.pack()  
    EntryCOM.delete(0, GUI.END) 

    # Restablecer el valor del Spinbox a 0
    SpinDATA.delete(0, "end")
    SpinDATA.insert(0, "0")  
    
    # Limpiar el texto del LabelRECIVE
    LabelRECIVE.config(text="dato recibido =")  

# Frame oculto inicialmente con los campos adicionales
campos = GUI.Frame(frame1)

# Instancia de los objetos
LabelCOM_NAME = GUI.Label(frame1, text="Escribe el nombre del puerto; ejem: COM2")
EntryCOM = GUI.Entry(frame1)
BotonCONECT = GUI.Button(frame1, text="CONECTAR", command=CONECTAR)

SpinDATA = GUI.Spinbox(campos, from_=0, to=500)
BotonSEND = GUI.Button(campos, text="ENVIAR", command=SEND)
LabelRECIVE = GUI.Label(campos, text="dato recibido =")
BotonCAmbiar = GUI.Button(campos, text='Cambiar Puerto', command=cambio)
BotonCerrar = GUI.Button(ventana, text="SALIR", command=CERRAR)

# Empaquetar los widgets iniciales
LabelCOM_NAME.pack(padx=1, pady=2)
EntryCOM.pack(padx=1, pady=2)
BotonCONECT.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)

# Empaquetar widgets dentro del frame `campos`
SpinDATA.pack(padx=1, pady=2)
BotonSEND.pack(padx=1, pady=2)
LabelRECIVE.pack(padx=1, pady=2)
BotonCAmbiar.pack(padx=1, pady=2)

# Iniciar el bucle principal
ventana.mainloop()