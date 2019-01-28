import pymysql



# datos de conexion
dbc = ("172.17.42.46","estudiante","estP53","netflix")

# Abrir conexion con MySQL
db = pymysql.connect(dbc[0],dbc[1],dbc[2],dbc[3])

# Obtener el cursor
cursor = db.cursor()
