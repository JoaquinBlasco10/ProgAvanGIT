# utils.py
import uuid
from typing import List

def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try: return int(input(mensaje))
        except ValueError: print("Entrada no válida.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try: return float(input(mensaje))
        except ValueError: print("Entrada no válida.")

def leer_cadena(mensaje="Introduce una cadena: "):
    while True:
        txt = input(mensaje).strip()
        if txt: return txt
        print("No puede estar vacío.")

def crear_menu(opciones: List[str]) -> int:
    for i, op in enumerate(opciones, 1):
        print(f"{i}. {op}")
    return leer_int("Selecciona una opción: ")

def generar_id(): return str(uuid.uuid4())[:8]
