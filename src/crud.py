from time import sleep
from src.datos import empresas,guardar_datos
from src.utils import pausa,titulo,limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR EMPRESA")
def registrar_alumno():
    pass
    
@pantalla("MOSTRAR EMPRESAS")
def mostrar_alumnos():
    for ruc,info in empresas.items():
        print(f"RUC : {ruc}")
        print(f"RAZON_SOCIAL : {info['razon_social']}")
        print(f"DIRECCIÓN : {info['direccion']}")
        print("*" * 50)
        
@pantalla("ACTUALIZAR EMPRESA")
def actualizar_alumno():
    pass
        
@pantalla("ELIMINAR EMPRESA")
def eliminar_alumno():
    pass
        
def menu_principal():
    while True:
        limpiar()
        titulo("CRUD DE EMPRESAS")
        print("""
            [1] REGISTRAR EMPRESA
            [2] MOSTRAR EMPRESA
            [3] ACTUALIZAR EMPRESA
            [4] ELIMINAR EMPRESA
            [5] SALIR
        """)
        
        opcion = int(input("INGRESE OPCIÓN : "))
        
        if opcion == 1:
            registrar_alumno()
            pausa()
        elif opcion == 2:
            mostrar_alumnos()
            pausa()
        elif opcion == 3:
            actualizar_alumno()
            pausa()
        elif opcion == 4:
            eliminar_alumno()
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