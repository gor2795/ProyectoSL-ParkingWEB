import tkinter as tk
from tkinter import messagebox
from tkinter import *
def validar():
    if (entrada1.get()=='pio' and entrada2.get()=='pio'):
        abrirventana2()
    else:
        messagebox.showwarning("Cuidado","Contraseña erronea")

def abrirventana2():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('300x300')
    win.configure(background='sea green')
    win.title("Parqueadero")


def cerrarventan():
    ventana.destroy()

ventana=tk.Tk()
ventana.title('Login')
ventana.geometry('230x230')
ventana.configure(background='dark turquoise')

e1=tk.Label(ventana,text="Usuario: ",bg='blue',fg='white')
e1.pack(padx=10,pady=10,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Contraseña: ",bg='blue',fg='white')
e2.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada2=tk.Entry(ventana)
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

boton=tk.Button(ventana,text="ventana nueva",fg="blue",command=abrirventana2)
boton.pack(side=tk.TOP)

boton3=tk.Button(ventana,text="Ingresar",fg="blue",command=validar)
boton3.pack(side=tk.TOP)
ventana.mainloop()