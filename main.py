from clases.DAO import Coneccion
import os
os.system('cls')
borrar=os.system("cls")

Cocection=Coneccion()

devMode=False


def MostrarUniversos():
    ListadoUniversos=Cocection.getUniversos()

    for uni in ListadoUniversos:
        print (f" {uni[0]}) {uni[1]}")
        
def InsertLuchador():
    NombreLuchador=input("Ingresar el nombre del Luchador: ")
    FechaNacimiento=input("Fecha de Nacimiento (YYYY-mm-dd): ")
    DescripcionPeleador=input("Descripcion del peleador: ")
    KI=input("Ingresar el KI del Luchador")
    

    ListadoUniversos=Cocection.getUniversos()

    for uni in ListadoUniversos:
        print (f" {uni[0]}) {uni[1]}")

    IdUniverso=input("Seleccionar el numero del universo del Luchador")

    Cocection.IngresoLuchador(NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso)
    

def MostrarLuchador():

    ListadoLuchadores=Cocection.getLuchadores()

    for uni in ListadoLuchadores:
        print (f"{uni[0]}) Luchador: {uni[1]} - Universo: {uni[6]}")

def ModificarLuchador():
    
    
    ListadoLuchadores=Cocection.getLuchadores()
    for uni in ListadoLuchadores:
        print (f"{uni[0]}) Luchador: {uni[1]} - Universo: {uni[6]}")
        
    LuchadorModificar=input("\n Seleccione jugador a modificar: \n") 


    NombreLuchador=input("Ingresar el nombre del Luchador: ")
    FechaNacimiento=input("Fecha de Nacimiento (YYYY-mm-dd): ")
    DescripcionPeleador=input("Descripcion del peleador: ")
    KI=input("Ingresar el KI del Luchador")
    MostrarUniversos()
    IdUniverso=input("Ingrese número de universo")
    Estado=input("Ingrese estado de jugador 1: activo / 0: inactivo")
    
    Cocection.ModificarLuchador(NombreLuchador,FechaNacimiento,DescripcionPeleador,KI,IdUniverso, Estado, LuchadorModificar)
    
def EliminarLuchador():
    ListadoLuchadores=Cocection.getLuchadores()
    for uni in ListadoLuchadores:
        print (f"{uni[0]}) Luchador: {uni[1]} - Universo: {uni[6]}")
        
    LuchadorModificar=int(input("\n Seleccione jugador a eliminar: \n"))
    
    Cocection.EliminarLuchador(LuchadorModificar)
    
    
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

    
if __name__=="__main__":
    #print(Cocection.Select('SELECT * from luchadores_dbz where NombreLuchador="1" or 1="1"'))

    while True:
        if devMode==True:
            print("Dev Mode: Activado \nPresione 5 para restaurar BD \n")
        
        print(""" MENU DE TORNEO: \n1.- Mantenedor luchadores  \n2.- Batallas  \n3.- Historico de Batallas \n4.- SALIR  """)
        OpcionMenu=input()

        if OpcionMenu=='1':
            CrudLuchadores()
            
        elif OpcionMenu=='2':
            pass   
        elif OpcionMenu=='3':
            pass    
        elif OpcionMenu=='4':
            print("Muchas gracias por utilizar el Sistema")
            break
        elif OpcionMenu=='5' and devMode==True:
            #DROP DATABASE `pruebas`;
            pass
        else:
            print("Opcion no valida")
        

        