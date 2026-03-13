from time import sleep
from src.datos import empresas,guardar_datos
from src.utils import pausa,titulo,limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR EMPRESA")
def registrar_empresa():
    ruc = input("INGRESE RUC : ")
    
    if ruc in empresas:
        print("YA EXISTE UNA EMPRESA CON ESE RUC.")
        return
    
    razon_social = input("INGRESE RAZON SOCIAL : ")
    direccion = input("INGRESE DIRECCIÓN : ")
    
    if not ruc or not razon_social or not direccion:
        print("TODOS LOS CAMPOS SON OBLIGATORIOS.")
        return
    
    empresas[ruc] = {
        "razon_social" : razon_social,
        "direccion" : direccion
    }
    guardar_datos(empresas)
    titulo("EMPRESA REGISTRADA CON ÉXITO")
     
    
@pantalla("MOSTRAR EMPRESAS")
def mostrar_empresas():
    if not empresas:
        print("NO HAY EMPRESAS REGISTRADAS.")
        return
    
    print("""
        [1] MOSTRAR TODAS LAS EMPRESAS
        [2] BUSCAR POR RUC    
    """)
    
    try:
        opcion = int(input("INGRESE OPCIÓN : "))
    except ValueError:
        print("OPCIÓN NO VÁLIDA")
        return
    
    if opcion == 1:
        print()
        for ruc,info in empresas.items():
            print(f"RUC : {ruc}")
            print(f"RAZON_SOCIAL : {info['razon_social']}")
            print(f"DIRECCIÓN : {info['direccion']}")
            print("=" * 50)
    elif opcion == 2:
        ruc = input("INGRESE RUC A BUSCAR : ")
        if ruc in empresas:
            info = empresas[ruc]
            print()
            print(f"RUC : {ruc}")
            print(f"RAZON_SOCIAL : {info['razon_social']}")
            print(f"DIRECCIÓN : {info['direccion']}")
            print("=" * 50)
        else:
            print("EMPRESA NO ENCONTRADA.")
    else:
        print("OPCIÓN NO VÁLIDA.")      
    
        
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
        guardar_datos(empresas)
        titulo("EMPRESA ACTUALIZADA CON ÉXITO")
    else:
        print("RUC NO ENCONTRADO.")
        
@pantalla("ELIMINAR EMPRESA")
def eliminar_empresa():
    ruc = input("INGRESE RUC DE LA EMPRESA A ELIMINAR : ")
    if ruc in empresas:
        print()
        print(f"EMPRESA ENCONTRADA : {empresas[ruc]['razon_social']}")
        print()
        print("[1] SI, ELIMINAR")
        print("[2] NO, CANCELAR")
        
        try:
            opcion = int(input("ESTA SEGURO QUE DESEA ELIMINAR ESTA EMPRESA? : "))
        except ValueError:
            print("OPCIÓN NO VÁLIDA. CANCELANDO ELIMINACIÓN.")
            return
        
        if opcion == 1:
            del empresas[ruc]
            guardar_datos(empresas)
            titulo("EMPRESA ELIMINADA CON ÉXITO")
        elif opcion == 2:
            print("OPERACIÓN CANCELADA.")
        else:
            print("OPCIÓN NO VÁLIDA. CANCELANDO ELIMINACIÓN.")
            
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
        print("=" * 50)
        
        try:
            opcion = int(input("INGRESE OPCIÓN : "))
        except ValueError:
            print("OPCIÓN NO VÁLIDA. DEBE INGRESAR UN NÚMERO.")
            pausa()
            continue
        
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