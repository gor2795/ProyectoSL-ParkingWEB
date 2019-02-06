from view import *
from view import abrirventana2

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
                        print()
                    else:
                        messagebox.showwarning("ERRROR", "Contraseña erronea")




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