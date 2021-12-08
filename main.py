from clases.DAO import Luchadores
import os
import time
import colorama
from colorama import Fore, Back, Style
os.system('cls')

Conexion=Luchadores()

devMode=True
def MostrarUniversos():
    ListadoUniversos=Conexion.getUniversos()

    for uni in ListadoUniversos:
        print (f" {uni[0]}) {uni[1]}")
        
def InsertLuchador():
    NombreLuchador=input("Ingresar el nombre del Luchador:  ")
    FechaNacimiento=input("Fecha de Nacimiento (YYYY-mm-dd):  ")
    DescripcionPeleador=input("Descripcion del peleador:  ")
    KI=input("Ingresar el KI del Luchador:  ")
    

    ListadoUniversos=Conexion.getUniversos()

    for uni in ListadoUniversos:
        print (f" {uni[0]}) {uni[1]}")

    IdUniverso=input("Seleccionar el numero del universo del Luchador:  ")
    skills=input("Ingresar habilidad del jugador:  ")
    salud=input("Ingresar puntos de vida del Luchador:  ")

    Conexion.IngresoLuchador(NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso, skills, salud)
    
def MostrarLuchador():

    ListadoLuchadores=Conexion.getLuchadores()
    for uni in ListadoLuchadores:
        if uni[3] == 1:   
            print (f"{uni[0]}) Luchador: {uni[1]} | Universo: {uni[6]}")
    
            
def ModificarLuchador():
    
        os.system('cls')
        ListadoLuchadores=Conexion.getLuchadores()
        for uni in ListadoLuchadores:
                print (f"{uni[0]}) Luchador: {uni[1]} - Universo: {uni[6]} Estado: {uni[3]}")
                
        LuchadorModificar=input("\n Seleccione jugador a modificar: \n")
        NombreLuchador=input("Ingresar el nombre del Luchador: ")
        FechaNacimiento=input("Fecha de Nacimiento (YYYY-mm-dd): ")
        DescripcionPeleador=input("Descripcion del peleador: ")
        KI=input("Ingresar el KI del Luchador")
        MostrarUniversos()
        IdUniverso=input("Ingrese número de universo")
        skills=input("Ingresar habilidad del jugador:  ")
        salud=input("Ingresar puntos de vida del Luchador:  ")
        Estado=input("Ingrese estado de jugador 1: activo / 0: inactivo")
    
        Conexion.ModificarLuchador(NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso, skills, salud, Estado,  LuchadorModificar)

def EliminarLuchador():
    ListadoLuchadores=Conexion.getLuchadores()
    for uni in ListadoLuchadores:
        if uni[3]==1:
            print (f"{uni[0]}) Luchador: {uni[1]} - Universo: {uni[6]}")
        
    LuchadorEliminar=int(input("\n Seleccione jugador a eliminar: \n"))
    
    Conexion.EliminarLuchador(LuchadorEliminar)
    
def CrudLuchadores():
    while True:
        print(""" \n CRUD Luchadores: 
        1.- Insertar Luchador  
        2.- Listar Luchadores  
        3.- Modificar Luchadores 
        4.- Eliminar Luchadores  
        5.- Volver Menu Principal   """)
        OpcionMenu=input()

        if OpcionMenu=='1':
           os.system("cls")
           InsertLuchador()
            
        elif OpcionMenu=='2':
           os.system("cls")
           MostrarLuchador()
              
        elif OpcionMenu=='3':
           os.system("cls")
           ModificarLuchador()
               
        elif OpcionMenu=='4':
            os.system("cls")
            EliminarLuchador()  
        else:
            break  
  
    
def AdminMode():
    
    while True:
        os.system("cls")
        print("""MENU ADMIN: 
        1.- Restaurar Base de datos. 
        2.- Eliminar  Base de datos. 
        0.- Volver Menu Principal   """)
        OpcionMenu=int(input())

        
        if OpcionMenu==1:
            resetconfirm=int(input(Back.RED+"¿Desea realmente restaurar la base de datos?\n Presione 1 para continuar"))
            if resetconfirm==1:
                #Conexion.VaciarDB()
                Conexion.restaurarDB()
            else:
                print("Ingrese un valor correcto.")
                time.sleep(2)
                
           
        elif OpcionMenu==2:
           Conexion.VaciarDB()
       
        elif OpcionMenu==0:
            os.system("cls")
            break    
        else:
            pass
            
if __name__=="__main__":
    #print(Conexion.Select('SELECT * from luchadores_dbz where NombreLuchador="1" or 1="1"'))
    colorama.init(autoreset=True)
    os.system("cls")
    while True:
        if devMode==True:
            print(Back.CYAN+"Dev Mode: Activado \n\nPresione 0 para acceder\nal menú de administrador. \n")
        
        print(""" MENU DE TORNEO: \n1.- Mantenedor luchadores  \n2.- Batallas  \n3.- Historico de Batallas \n4.- SALIR  """)
        OpcionMenu=input()

        if OpcionMenu=='1':
            CrudLuchadores()
            
        elif OpcionMenu=='2':
            pass   
        elif OpcionMenu=='3':
            pass    
        elif OpcionMenu=='0' and devMode == True:
            AdminMode()
        elif OpcionMenu=='4':
            print("Muchas gracias por utilizar el Sistema")
            break
        
       
        else:
            print("Opción no valida. Por favor Reintente.")
            time.sleep(2)
            os.system("cls")