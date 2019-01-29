from tkinter import *

def calcular():
    v2.set(str(int(numero.get())/2)+" dolar(es)")

root = Tk()
root.title("Ventana 1")
root.geometry("700x600+0+0")

v2=StringVar()
numero=StringVar()
et1 = Label (root,text="Ingrese el numero de horas (0.50$ hora o fracción ): ").grid(row=0, column=1)
lbhoras = Entry(root,textvariable=numero).grid(row=0, column=2)
btn2 = Button(root, text="Confirmar",comman=calcular)
btn2.grid(row=0, column=3)
lblM3 = Label (root,text="El total a pagar es: ").grid(row=2, column=1)
lblPagar = Label (root,textvariable=v2).grid(row=2, column=2)

root.mainloop()