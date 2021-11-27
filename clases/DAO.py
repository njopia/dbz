from mysql import connector
import mysql.connector
from mysql.connector import Error

host="localhost",
user="root",
password="",
port=3306,
database="dragonballtorneo"

class Coneccion:
    def __init__(self):
        try:

            self.conector=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port=3306,
                database="dragonballtorneo"
         
           )
        except Error as ex:
            print (f"Existe un error en la conexion de la BD: {ex}")
    
        
    def Select(self,Query): #Método que usaremos para realizar un Select a la tabla especificada en main(query)
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                
                cursor.execute(Query)
                return cursor.fetchall()
                
                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")
   
    def Insert(self,sqlInsert,ParametrosIngreso): #Método que usaremos para realizar un INSERT a la tabla especificada en main(query)
       if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                cursor.execute(sqlInsert,ParametrosIngreso)
                self.conector.commit() 
                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")

    def getUniversos(self):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                sql="select * from universos_dbz"
                cursor.execute(sql)
                return cursor.fetchall()
                
                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")
                
    def getLuchadores(self):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                sql="select * from luchadores_dbz"
                cursor.execute(sql)
                return cursor.fetchall()
                
                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")

    def IngresoLuchador(self,NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                sqlInsert="INSERT INTO luchadores_dbz ( NombreLuchador, FechaNacimiento, SwEstado, DescripcionPeleador, KI, IdUniverso) VALUES (%s, %s, %s, %s, %s, %s);"
                ParametrosIngreso=(NombreLuchador,FechaNacimiento, 1, DescripcionPeleador,KI,IdUniverso)
                cursor.execute(sqlInsert,ParametrosIngreso)
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea

                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")

    def ModificarLuchador(self,NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso, Estado, LuchadorModificar):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                sqlUpdate="UPDATE luchadores_dbz SET NombreLuchador = %s, FechaNacimiento = %s,  DescripcionPeleador = %s, KI = %s, IdUniverso = %s, SwEstado = %s WHERE luchadores_dbz.IdLuchador = %s;"
                
                #sqlInsert="INSERT INTO luchadores_dbz ( NombreLuchador, FechaNacimiento, SwEstado, DescripcionPeleador, KI, IdUniverso) VALUES (%s, %s, %s, %s, %s, %s);"
                
                ParametrosIngreso=(NombreLuchador,FechaNacimiento, DescripcionPeleador,KI,IdUniverso,Estado, LuchadorModificar)
                
                
                cursor.execute(sqlUpdate,ParametrosIngreso)
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea

                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")
                
    def EliminarLuchador(self,LuchadorModificar):
        if self.conector.is_connected():
            try:
                print("Jugador es:   ",LuchadorModificar)
                cursor=self.conector.cursor()
                sqlDelete="DELETE FROM luchadores_dbz WHERE luchadores_dbz.IdLuchador = %s;"
                
                ParametrosIngreso=(LuchadorModificar, ) #Mantener la comma posterior a la variable. Solo en DELETE
                
                
                cursor.execute(sqlDelete,ParametrosIngreso)
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea

                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")