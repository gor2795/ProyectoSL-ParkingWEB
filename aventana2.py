from tkinter import *
import tkinter as tk
from tkinter import messagebox



ventana = Tk()
ventana.title("Elija donde estacionarse")
pusuario=StringVar()
pcontraseña=StringVar()
ventana.geometry("500x300")

et1= Label (ventana,text="horas a estacionarse: ").grid(row=1, column=1)
lbNombre= Entry(ventana,textvariable=pusuario).grid(row=6, column=10)

boton = tk.Button(ventana, text="parqueadero1",).grid(row=1,column=15)
boton1 = tk.Button(ventana, text="parqueadero1",).grid(row=2,column=15)
boton2 = tk.Button(ventana, text="parqueadero1",).grid(row=3,column=15)
boton3 = tk.Button(ventana, text="parqueadero1",).grid(row=4,column=15)
ventana.mainloop()