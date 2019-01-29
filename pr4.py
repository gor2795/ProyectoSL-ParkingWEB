from tkinter import *
state=True
def change(event):
    global state
    if state == True:
        lbl1.config(image= btnFalse)
        print("Opcion falsa")
        state=False
        num="1"
    else:
        lbl1.config(image= btnTrue)
        print("Opcion verdadera")
        state=True
        num="Ninguno"
    v1.set(num)


root = Tk()
root.title("Ventana 1")
root.geometry("700x600+0+0")
btnFalse= PhotoImage(file="ima\ddd.gif")
btnTrue= PhotoImage(file="ima\logo.gif")
lbl1 = Label(root,image=btnTrue)
lbl1.bind('<Button>',change)
lbl1.place(x=200,y=200)

v1 = StringVar()
lblM2 = Label (root,text="Usted a elegido el lugar: ").grid(row=1, column=1)
lblLugar = Label (root,textvariable=v1).grid(row=1, column=2)

root.mainloop()