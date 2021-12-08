import mysql.connector
from mysql.connector import Error
import time
import os
class Luchadores:
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

    def IngresoLuchador(self,NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso, skills, salud):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                sqlInsert="INSERT INTO luchadores_dbz ( NombreLuchador, FechaNacimiento, SwEstado, DescripcionPeleador, KI, IdUniverso, habilidades, salud) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                ParametrosIngreso=(NombreLuchador,FechaNacimiento, 1, DescripcionPeleador,KI,IdUniverso,skills,salud)
                cursor.execute(sqlInsert,ParametrosIngreso)
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea

                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")

    def ModificarLuchador(self,NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso, skills,salud, Estado, LuchadorModificar):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                sqlUpdate="UPDATE luchadores_dbz SET NombreLuchador = %s, FechaNacimiento = %s,  DescripcionPeleador = %s, KI = %s, IdUniverso = %s, habilidades=%s, salud = %s,SwEstado = %s WHERE luchadores_dbz.IdLuchador = %s;"
                
                #sqlInsert="INSERT INTO luchadores_dbz ( NombreLuchador, FechaNacimiento, SwEstado, DescripcionPeleador, KI, IdUniverso) VALUES (%s, %s, %s, %s, %s, %s);"
                
                ParametrosIngreso=(NombreLuchador,FechaNacimiento, DescripcionPeleador,KI,IdUniverso, skills, salud, Estado, LuchadorModificar)
                
                
                cursor.execute(sqlUpdate,ParametrosIngreso)
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea

                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")
                
    def EliminarLuchador(self,LuchadorEliminar):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                sqlDelete="UPDATE luchadores_dbz SET SwEstado = 0 WHERE luchadores_dbz.IdLuchador = %s;"
                
                ParametrosIngreso=(LuchadorEliminar, ) #Mantener la comma posterior a la variable. Solo en DELETE
                
                
                cursor.execute(sqlDelete,ParametrosIngreso)
                print(f"El jugador N° {LuchadorEliminar} ha sido eliminado exitosamente")
                time.sleep(2)
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea

                
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")
    
    def VaciarDB(self):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                foreignCheck0="SET FOREIGN_KEY_CHECKS = 0;"
                sqlTruncLuchadores="TRUNCATE luchadores_dbz;"
                sqlTruncUniversos="TRUNCATE universos_dbz;"
                foreignCheck1="SET FOREIGN_KEY_CHECKS = 1;"
                cursor.execute(foreignCheck0)
                cursor.execute(sqlTruncLuchadores)
                cursor.execute(sqlTruncUniversos)
                cursor.execute(foreignCheck1)
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea
                print("Las filas han sido eliminadas exitosamente")
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")        
                
    def restaurarDB(self):
        if self.conector.is_connected():
            try:
                cursor=self.conector.cursor()
                
                createLuchadorTB="CREATE TABLE IF NOT EXISTS luchadores_dbz (IdLuchador INT (11) NOT NULL, NombreLuchador varchar(10) COLLATE utf8_spanish_ci NOT NULL, FechaNacimiento date NOT NULL, SwEstado tinyint(1) NOT NULL, DescripcionPeleador text COLLATE utf8_spanish_ci NOT NULL,KI int(11) NOT NULL,IdUniverso smallint(6) NOT NULL,habilidades varchar(28) COLLATE utf8_spanish_ci NOT NULL,salud varchar(11) COLLATE utf8_spanish_ci NOT NULL);"
                
                createUniversosTB="CREATE TABLE IF NOT EXISTS universos_dbz (IdUniverso smallint(6) NOT NULL, Universo varchar(50) COLLATE utf8_spanish_ci NOT NULL, SwEstado tinyint(1) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;"
                
                sqlFillLuchadores = "INSERT INTO `luchadores_dbz` (`NombreLuchador`, `FechaNacimiento`, `SwEstado`, `DescripcionPeleador`, `KI`, `IdUniverso`, `habilidades`, `salud`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                
                
                valuesFillLuchadores = [
                    ('Goku', '2021-11-17', 1, 'Son Gokū es un personaje ficticio, protagonista de la serie de manga y anime Dragon Ball.', 9999, 7, 'Kame Hame Ha', '100000'),
                    ('Freezer', '2021-11-12', 1, 'Puede transformarse en varias formas para esconder su poder de combate y poder darle uso en situaciones de riesgo.', 85000, 7, 'Death Ball', '90000'),
                    ('Vegeta', '2021-11-21', 1, 'Vegeta, también conocido como Príncipe Vegeta. Es el príncipe de una raza guerrera extraterrestre conocida como los Saiyajin. Es extremadamente arrogante, orgulloso y trabajador; constantemente se refiere a su herencia y estatus real', 95000, 7, 'Garlick Gun', '90000'),
                    ('Piccolo', '2021-11-29', 1, 'Primero se lo ve como la reencarnación del malvado Piccolo Daimaō  Sin embargo, más tarde se revela que él es un miembro de una especie humanoide extraterrestre llamada Namekuseijins, seres capaces de crear las esferas del dragón capaces de conceder deseo.', 75000, 7, 'Makosen', '65000'),
                    ('Beerus', '2012-11-14', 1, 'Beerus es un dios destructor del universo 7. A menudo visto destruyendo planetas por capricho, los dos únicos deseos de Beerus son ser todo un gourmet, disfrutar de la comida que le gusta comer y luchar contra oponentes a quienes considera dignos', 500000, 7, 'Hakai', '500000'),
                    ('Zeno Sama', '2021-08-17', 1, 'El Rey de Todo, también conocido como Zen Oo  y apodado por Son Goku como Todito , es el gobernante y dios absoluto de todos los universos y el máximo soberano de todo lo existente en Dragon Ball.', 999999999, 0, 'Aniquilacion Absoluta', '999999999'),
                    ('Jiren', '2021-11-16', 1, 'Jiren es uno de los miembros de las Tropas del Orgullo, soldados justicieros provenientes del Universo 11 y que participa en el Torneo de la Fuerza.', 230000, 11, 'Power Impact', '170000'),
                    ('Caulifla', '2021-11-13', 1, 'Es una saiyana del Planeta Sadala del Universo 6. Es una joven delincuente, líder de una pandilla, que fue reclutada por Cabba para ser miembro del Equipo del Universo 6 para participar en el Torneo de la Fuerza.', 98000, 6, 'Estallido Devastador', '90000')
                ]
                
                sqlFillUniversos = "INSERT INTO `universos_dbz` (`Universo`, `SwEstado`) VALUES (%s, %s)"
                
                valuesFillUniversos = [      
                    ('Indeterminado', 1),
                    ('Universo 1', 1),
                    ('Universo 2', 1),
                    ('Universo 3', 1),
                    ('Universo 4', 1),
                    ('Universo 5', 1),
                    ('Universo 6', 1),
                    ('Universo 7', 1),
                    ('Universo 8', 1),
                    ('Universo 9', 1),
                    ('Universo 10', 1),
                    ('Universo 11', 1)
                    ]
                
                
                #PrimaryLuchador="ALTER TABLE luchadores_dbz ADD PRIMARY KEY (IdLuchador), ADD KEY FK_IdUniverso (IdUniverso);"
                
                #PrimaryUniversos="ALTER TABLE universos_dbz ADD PRIMARY KEY (IdUniverso);"
                
                #AutoIncrementLuchadores="ALTER TABLE luchadores_dbz MODIFY IdLuchador int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;"
                
                #AutoIncrementUniversos="ALTER TABLE universos_dbz  MODIFY IdUniverso smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;"

                #AddForeignKeys="ALTER TABLE luchadores_dbz  ADD CONSTRAINT FK_IdUniverso FOREIGN KEY (IdUniverso) REFERENCES universos_dbz (IdUniverso) ON DELETE CASCADE ON UPDATE CASCADE;"




                foreignCheck0="SET FOREIGN_KEY_CHECKS = 0;"
                foreignCheck1="SET FOREIGN_KEY_CHECKS = 1;"
                
                cursor.execute(foreignCheck0)
                
                cursor.execute(createLuchadorTB)
                cursor.execute(createUniversosTB)
                
                cursor.executemany(sqlFillLuchadores,valuesFillLuchadores)
                cursor.executemany(sqlFillUniversos,valuesFillUniversos)
                
                cursor.execute(foreignCheck1)
                
                
                """ cursor.execute(PrimaryLuchador)
                cursor.execute(PrimaryUniversos)
                cursor.execute(AutoIncrementLuchadores)
                cursor.execute(AutoIncrementUniversos)
                cursor.execute(AddForeignKeys) """
                
                self.conector.commit() # Cuando se escribe,Updatea y elimina la info de commitea
                print(f" \n Las filas han sido insertadas exitosamente.")
                time.sleep(2)
                os.system("cls")
            except Error as ex:
                print (f"Existe un error en la conexion de la BD: {ex}")            