import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV = os.path.join(BASE_DIR, "..", "empresas.csv")

def cargar_datos():
    datos = {}

    if os.path.exists(ARCHIVO_CSV):
        try:
            with open(ARCHIVO_CSV, mode="r", encoding="utf-8", newline="") as archivo:
                lector = csv.DictReader(archivo)

                for fila in lector:
                    ruc = fila["ruc"]
                    datos[ruc] = {
                        "razon_social": fila["razon_social"],
                        "direccion": fila["direccion"]
                    }
        except Exception as e:  
            print(f"ERROR AL CARGAR DATOS: {e}")
    return datos

def guardar_datos(datos):
    try:
        with open(ARCHIVO_CSV, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["ruc", "razon_social", "direccion"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            escritor.writeheader()

            for ruc, info in datos.items():
                escritor.writerow({
                    "ruc": ruc,
                    "razon_social": info["razon_social"],
                    "direccion": info["direccion"]
                })
    except Exception as e:
        print(f"ERROR AL GUARDAR DATOS: {e}")
empresas = cargar_datos()