import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import font
import pymysql
# datos de conexion
dbc = ("localhost","root","jokernnt","db_parking")

# Abrir conexion con MySQL
db = pymysql.connect(dbc[0],dbc[1],dbc[2],dbc[3])

# Obtener el cursor
cursor = db.cursor()
def validar():
    if entrada1.get() == "":
        messagebox.showwarning("AVISO", "EL campo Usuario está vacio")
    else:
        sql = "SELECT pass from registro WHERE nombre_u='%s'" % \
              (entrada1.get())
        if cursor.execute(sql) == 0:
            messagebox.showwarning("ERROR", "El usuario no existe")
        else:
            if entrada2.get() == "":
                messagebox.showwarning("AVISO", "EL campo Contraseña está vacio")
            else:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    if row[0] == entrada2.get():
                        abrirventana2()
                    else:
                        messagebox.showwarning("ERRROR", "Contraseña erronea")


def abrirventana2():
    #cambio botones
    def mens1(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn1.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn1.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens2(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn2.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn2.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens3(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn3.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn3.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens4(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn4.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn4.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens5(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn5.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn5.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens6(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn6.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn6.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens7(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn7.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn7.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens8(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn8.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn8.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens9(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn9.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn9.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens10(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn10.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn10.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens11(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn11.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn11.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")

    def mens12(num):
        if v1.get() == "0":
            resultaado = messagebox.askquestion("Comprobar", message="Desea seleccionar este espacio?")
            if resultaado == "yes":
                btn12.config(image=btnFalse)
                v1.set(num)
        else:
            if v1.get() == num:
                retro = messagebox.askquestion("Cambiar", message="Desea cambiar este espacio?")
                if retro == "yes":
                    btn12.config(image=btnTrue)
                    num = "0"
                    v1.set(num)
            else:
                messagebox.showwarning("ERROR", "Ya hay un espacio escogido")


    def calcular():
        v2.set(str(int(numero.get()) / 2))

    def insertar():
        lugar = v1.get()
        n_horas = numero.get()
        v_pagar = v2.get()
        sql = "INSERT INTO parqueadero(lugar, \
                 user,horas,pago) \
                VALUES('%s','%s', '%s', '%s')" % \
              (lugar,entrada1.get(), n_horas, v_pagar)
        try:
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo("Guardado", "Se ha registrado exitosamente")
            db.close()
        except:
            messagebox.showwarning("ERRROR", "Ya se ha ingresdo el registro")


    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('700x600+0+0')
    win.configure(background='SteelBlue')
    win.title("Parqueadero")
    btnFalse = PhotoImage(file="ima\pfalse.png")
    btnTrue = PhotoImage(file="ima\ptrue.png")

    btn1 = Button(win, image=btnTrue, comman=lambda i="1": mens1(i))
    btn1.place(x=10, y=200)

    btn2 = Button(win, image=btnTrue, comman=lambda i="2": mens2(i))
    btn2.place(x=120, y=200)

    btn3 = Button(win, image=btnTrue, comman=lambda i="3": mens3(i))
    btn3.place(x=230, y=200)

    btn4 = Button(win, image=btnTrue, comman=lambda i="4": mens4(i))
    btn4.place(x=340, y=200)

    btn5 = Button(win, image=btnTrue, comman=lambda i="5": mens5(i))
    btn5.place(x=450, y=200)

    btn6 = Button(win, image=btnTrue, comman=lambda i="6": mens6(i))
    btn6.place(x=560, y=200)

#botoes abajo
    btn7 = Button(win, image=btnTrue, comman=lambda i="7": mens7(i))
    btn7.place(x=10, y=310)

    btn8 = Button(win, image=btnTrue, comman=lambda i="8": mens8(i))
    btn8.place(x=120, y=310)

    btn9 = Button(win, image=btnTrue, comman=lambda i="9": mens9(i))
    btn9.place(x=230, y=310)

    btn10 = Button(win, image=btnTrue, comman=lambda i="10": mens10(i))
    btn10.place(x=340, y=310)

    btn11 = Button(win, image=btnTrue, comman=lambda i="11": mens11(i))
    btn11.place(x=450, y=310)

    btn12 = Button(win, image=btnTrue, comman=lambda i="12": mens12(i))
    btn12.place(x=560, y=310)

    # Bloqueo de espacios escogidos
    sql = "SELECT lugar from parqueadero"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[0] == "1":
            btn1.config(image=btnFalse, state='disabled')
        if row[0] == "2":
            btn2.config(image=btnFalse, state='disabled')
        if row[0] == "3":
            btn3.config(image=btnFalse, state='disabled')
        if row[0] == "4":
            btn4.config(image=btnFalse, state='disabled')
        if row[0] == "5":
            btn5.config(image=btnFalse, state='disabled')
        if row[0] == "6":
            btn6.config(image=btnFalse, state='disabled')
        if row[0] == "7":
            btn7.config(image=btnFalse, state='disabled')
        if row[0] == "8":
            btn8.config(image=btnFalse, state='disabled')
        if row[0] == "9":
            btn9.config(image=btnFalse, state='disabled')
        if row[0] == "10":
            btn10.config(image=btnFalse, state='disabled')
        if row[0] == "11":
            btn11.config(image=btnFalse, state='disabled')
        if row[0] == "12":
            btn12.config(image=btnFalse, state='disabled')


    v1 = StringVar()
    v1.set("0")
    v2 = StringVar()
    numero = StringVar()
    numero.set("0")
    helvfont = font.Font(family="arial", size=12, weight="bold")
    et1 = tk.Label(win, text="Ingrese el numero de horas (0.50$ hora o fracción ):   ", bg='Steel Blue', fg='white',
                   font=helvfont).grid(row=0, column=1)
    lbhoras = Entry(win, textvariable=numero).grid(row=0, column=2)
    btnc = Button(win, text="Confirmar", bg='blue', fg='white', comman=calcular)
    btnc.grid(row=0, column=3)
    lblM2 = Label(win, text="Usted a elegido el lugar: ", bg='Steel Blue', fg='white', font=helvfont).grid(row=1,
                                                                                                           column=1)
    lblLugar = Label(win, textvariable=v1, bg='Steel Blue', fg='white', font=helvfont).grid(row=1, column=2)
    lblM3 = Label(win, text="El total a pagar es: ", bg='Steel Blue', fg='white', font=helvfont).grid(row=2, column=1)
    lblPagar = Label(win, textvariable=v2, bg='Steel Blue', fg='white', font=helvfont).grid(row=2, column=2)
    w = Spinbox(win, textvariable=numero, from_=1, to=10, state='readonly').grid(row=0, column=2)



    boton2 = tk.Button(win, text='SALIR', command=win.destroy)
    boton2.place(x=600,y=500)

    boton3 = tk.Button(win, text='CONFIRMAR', command=insertar)
    boton3.place(x=500, y=500)

def abrirventana3():
    # datos de conexion
    dbc = ("localhost", "root", "jokernnt", "db_parking")

    # Abrir conexion con MySQL
    db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])

    # Obtener el cursor
    cursor = db.cursor()

    sql = "SELECT nombre_u from registro WHERE nombre_u='jorge'"
    print(cursor.execute(sql))

    def reg():
        if entrada1.get() == "":
            messagebox.showwarning("AVISO", "EL campo Usuario está vacio")
        else:
            sql = "SELECT nombre_u from registro WHERE nombre_u='%s'" % \
                  (entrada1.get())
            print(cursor.execute(sql))
            if cursor.execute(sql) == 1:
                messagebox.showwarning("ERROR", "El usuario ya existe")
            else:
                if entrada2.get() == "":
                    messagebox.showwarning("AVISO", "EL campo Contraseña está vacio")
                else:
                    if entrada2.get() == entrada3.get():
                        sql = "INSERT INTO registro(nombre_u, \
                                         pass) \
                                        VALUES('%s','%s')" % \
                              (entrada1.get(), entrada2.get())
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()
                        messagebox.showinfo("Guardado", "Se ha registrado exitosamente")
                        db.close()
                    else:
                        messagebox.showwarning("AVISO", "Las contraseñas no coinciden")

    ventana.withdraw()
    win1 = tk.Toplevel()
    win1.geometry('300x300')
    imagen1 = PhotoImage(file="ima\login2.png")
    fondo1 = Label(win1, image=imagen1).place(x=0, y=0)
    win1.configure(background='sea green')
    win1.title('Registro')
    helvfont = font.Font(family="arial", size=15, weight="bold")

    e1 = tk.Label(win1, text="Usuario: ", bg='RoyalBlue4', fg='white', font=helvfont)

    e1.pack(padx=5, pady=5, ipadx=5, ipady=5)

    entrada1 = tk.Entry(win1)
    entrada1.pack(fill=tk.Y, padx=5, pady=5, ipadx=5, ipady=5)

    e2 = tk.Label(win1, text="Contraseña: ", bg='RoyalBlue4', fg='white', font=helvfont)
    e2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada2 = tk.Entry(win1, show="\u2022")
    entrada2.pack(fill=tk.Y, padx=5, pady=5, ipadx=5, ipady=5)

    e3 = tk.Label(win1, text="Confirme Contraseña: ", bg='RoyalBlue4', fg='white', font=helvfont)
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada3 = tk.Entry(win1, show="\u2022")
    entrada3.pack(fill=tk.Y, padx=5, pady=5, ipadx=5, ipady=5)

    boton3 = tk.Button(win1, text="Ingresar", fg="blue", command=reg, font=helvfont)
    boton3.pack(padx=5, pady=5, ipadx=5, ipady=5)

    win1.mainloop()


ventana=tk.Tk()
ventana.title('Login')
ventana.geometry('300x300')
imagen=PhotoImage(file="ima\yy.png")
fondo=Label(ventana,image=imagen).place(x=0,y=0)
helvfont = font.Font(family="arial", weight="bold")
ventana.configure(background='dark turquoise')

e1=tk.Label(ventana,text="Usuario: ",bg='RoyalBlue4',fg='white',font=helvfont)
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.Y,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Contraseña: ",bg='RoyalBlue4',fg='white',font=helvfont)
e2.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada2=tk.Entry(ventana,show="\u2022")
entrada2.pack(fill=tk.Y,padx=5,pady=5,ipadx=5,ipady=5)
boton3=tk.Button(ventana,text="Ingresar",fg="blue",command=validar,font=helvfont)
boton3.pack(side=tk.TOP)
boton33=tk.Button(ventana,text="Crear Usuario",fg="blue",command=abrirventana3,font=helvfont)
boton33.pack(side=tk.TOP)
ventana.mainloop()