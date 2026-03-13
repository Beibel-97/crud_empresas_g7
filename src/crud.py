from time import sleep
from src.datos import empresas,guardar_datos
from src.utils import pausa,titulo,limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR EMPRESA")
def registrar_empresa():
    ruc = input("INGRESE RUC : ")
    razon_social = input("INGRESE RAZON SOCIAL : ")
    direccion = input("INGRESE DIRECCIÓN : ")
    
    empresas[ruc] = {
        "razon_social" : razon_social,
        "direccion" : direccion
    }
    titulo("EMPRESA REGISTRADA CON ÉXITO")    
    
@pantalla("MOSTRAR EMPRESAS")
def mostrar_alumnos():
    for ruc,info in empresas.items():
        print(f"RUC : {ruc}")
        print(f"RAZON_SOCIAL : {info['razon_social']}")
        print(f"DIRECCIÓN : {info['direccion']}")
        print("*" * 50)
        
@pantalla("ACTUALIZAR EMPRESA")
def actualizar_empresa():
    ruc = input("INGRESE RUC DE LA EMPRESA A ACTUALIZAR : ")
    if ruc in empresas:
        razon_social = input("INGRESE NUEVA RAZON SOCIAL : ")
        direccion = input("INGRESE NUEVA DIRECCIÓN : ")
        empresas[ruc] = {
            "razon_social" : razon_social,
            "direccion" : direccion
        }
        titulo("EMPRESA ACTUALIZADA CON ÉXITO")
    else:
        print("RUC NO ENCONTRADO.")
        
@pantalla("ELIMINAR EMPRESA")
def eliminar_empresa():
    ruc = input("INGRESE RUC DE LA EMPRESA A ELIMINAR : ")
    if ruc in empresas:
        del empresas[ruc]
        titulo("EMPRESA ELIMINADA CON ÉXITO")
    else:
        print("RUC NO ENCONTRADO.")

def menu_principal():
    while True:
        limpiar()
        titulo("CRUD DE EMPRESAS")
        print("""
            [1] REGISTRAR EMPRESA
            [2] MOSTRAR EMPRESAS
            [3] ACTUALIZAR EMPRESA
            [4] ELIMINAR EMPRESA
            [5] SALIR
        """)
        
        opcion = int(input("INGRESE OPCIÓN : "))
        
        if opcion == 1:
            registrar_empresa()
            pausa()
        elif opcion == 2:
            mostrar_empresas()
            pausa()
        elif opcion == 3:
            actualizar_empresa()
            pausa()
        elif opcion == 4:
            eliminar_empresa()
            pausa()
        elif opcion == 5:
            guardar_datos(empresas)
            limpiar()
            titulo("SALIENDO DEL SISTEMA...")
            print("Datos guardados en empresas.csv")
            sleep(2)
            break
        else:
            print("Opción no válida.")