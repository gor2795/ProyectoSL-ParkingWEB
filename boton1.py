from tkinter import *
state=False
def change(event):
    global state
    if state == True:
        lbl1.config(image= btnFalse)
        print("Opcion falsa")
        state=False
    else:
        lbl1.config(image= btnTrue)
        print("Opcion verdadera")
        state=True

root = Tk()
root.title("Ventana 1")
root.geometry("700x600+0+0")
btnFalse= PhotoImage(file="ima\ddd.gif")
btnTrue= PhotoImage(file="ima\logo.gif")
lbl1 = Label(root,image=btnFalse)
lbl1.bind('<Button>',change)
lbl1.place(x=200,y=200)
root.mainloop()