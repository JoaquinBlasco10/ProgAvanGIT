
from typing import List, Dict
import uuid

def leer_int(mensaje: str) -> int:
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Se esperaba un número entero.")

def leer_float(mensaje: str) -> float:
    try:
        return float(input(mensaje))
    except ValueError:
        raise ValueError("Se esperaba un número decimal.")

def crear_menu(opciones: List[str]) -> int:
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    return leer_int("Seleccione una opción: ")

def generar_id() -> str:
    return str(uuid.uuid4())[:8]
