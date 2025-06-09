# utils.py
import uuid
from typing import List

def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try: return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try: return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número decimal.")

def crear_menu(opciones_menu: List[str]) -> int:
    print("\nMenú:")
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    return leer_int("Selecciona una opción: ")

def generar_id() -> str:
    return str(uuid.uuid4())[:8]
