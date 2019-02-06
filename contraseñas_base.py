import pymysql
# datos de conexion
dbc = ("localhost","root","jokernnt","base_park")

# Abrir conexion con MySQL
db = pymysql.connect(dbc[0],dbc[1],dbc[2],dbc[3])

# Obtener el cursor
cursor = db.cursor()
def comparacion(id,cont):
    sql = "SELECT pass from registro WHERE nombre_u='%s'" % \
          (id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            if row[0] == cont:
                print("correcto")
            else:
                print("Los campos no coinciden")
    except:
        print("Error: unable to generos")

comparacion("jorge","jokernnt")