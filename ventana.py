from tkinter import *
import tkinter as tk
from tkinter import messagebox

def validar():
    if et2.get ()=='1234':
        aventana2()
    else:
        messagebox.showwarning("contraseña incorrecta")

def aventana2():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('300x500')
    win.configure(background='black')
    e3=tk.Label(win,text="bienvenido")

ventana = Tk()
ventana.title("Parking Web")
pusuario=StringVar()
pcontraseña=StringVar()
ventana.geometry("500x300")

et1= Label (ventana,text="Usuario: ").grid(row=1, column=1)
lbNombre= Entry(ventana,textvariable=pusuario).grid(row=1, column=10)
et2= Label (ventana,text="Contraseña").grid(row=2, column=1)
lbResumen= Entry(ventana,textvariable=pcontraseña).grid(row=2, column=10)
boton = tk.Button(ventana, text="Iniciar Sesión",comand=aventana2()).grid(row=5,column=15)
boton.pack(side=tk.TOP)
ventana.mainloop()