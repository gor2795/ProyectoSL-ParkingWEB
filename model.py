import pymysql
# datos de conexion
dbc = ("localhost","root","jokernnt","db_parking")

# Abrir conexion con MySQL
db = pymysql.connect(dbc[0],dbc[1],dbc[2],dbc[3])

# Obtener el cursor
cursor = db.cursor()