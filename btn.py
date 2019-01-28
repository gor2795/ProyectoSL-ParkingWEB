from tkinter import *
from tkinter import messagebox


def mens():
    resultaado=messagebox.askquestion("Comprobar",message="Desea seleccionar este espacio?")
    if resultaado == "yes":
        btn1.config(image= btnFalse)
    else:
        btn1.config(image= btnTrue)


root = Tk()
root.title("Ventana 1")
root.geometry("700x600+0+0")
btnFalse= PhotoImage(file="ima\ddd.gif")
btnTrue= PhotoImage(file="ima\logo.gif")
btn1 = Button(root, image=btnTrue, comman=mens)
btn1.place(x=20,y=200)

root.mainloop()