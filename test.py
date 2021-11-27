import mysql.connector
import os
os.system("cls")

conector=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="dragonball"
)

cursor=conector.cursor()
sql="select * from universos_dbz"
cursor.execute(sql)
mysqlResultador=cursor.fetchall()


listDatos=[]
for c in mysqlResultador:
    diccionarioUniversos={
        'idUniverso':c[0],
        'NombreUniverso':c[1]
    }
    listDatos.append(diccionarioUniversos)

print(listDatos[4]['NombreUniverso'])





    # print(f'ID {c[0]} | Universo {c[1]}')


    # Tarea:
    #     Crear para cada resultado de la query, un diccionario de datos, para posterior, consultar un dato por
    #     una keyNombre en vez de un Indice