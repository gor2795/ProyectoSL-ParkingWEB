import pymysql
# datos de conexion
dbc = ("172.17.42.46","estudiante","estP53","netflix")

# Abrir conexion con MySQL
db = pymysql.connect(dbc[0],dbc[1],dbc[2],dbc[3])

# Obtener el cursor
cursor = db.cursor()
def comparacion(id,cont):
    sql = "SELECT name from genre WHERE id_genre='%d'" % \
          (int(id))
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