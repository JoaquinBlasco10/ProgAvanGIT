# main.py
from empleado import Empleado
from cliente import Cliente
from registro import RegistroDiario
from time import Time
from utils import leer_cadena, leer_int, crear_menu

registro = RegistroDiario()
otro_registro = RegistroDiario()

def leer_hora():
    h = leer_int("Hora: ")
    m = leer_int("Minuto: ")
    s = leer_int("Segundo: ")
    return Time(h, m, s)

def introducir_empleado():
    nom = leer_cadena("Nombre: ")
    edad = leer_int("Edad: ")
    nacio = leer_hora()
    cat = leer_cadena("Categoría: ")
    antig = leer_int("Antigüedad: ")
    registro.agregar_persona(Empleado(nom, edad, nacio, cat, antig))

def introducir_cliente():
    nom = leer_cadena("Nombre: ")
    edad = leer_int("Edad: ")
    nacio = leer_hora()
    dni = leer_cadena("DNI: ")
    registro.agregar_persona(Cliente(nom, edad, nacio, dni))

def buscar_persona():
    nom = leer_cadena("Nombre a buscar: ")
    edad = leer_int("Edad: ")
    for p in registro._personas:
        if p.nombre == nom and p.edad == edad:
            print("Empleado:" if registro.es_empleado(p) else "Cliente:")
            p.visualizar()
            return
    print("Persona no encontrada.")

def visualizar_por_indice():
    i = leer_int("Índice: ")
    if 0 <= i < len(registro._personas):
        registro[i].visualizar()
    else:
        print("Índice fuera de rango.")

def combinar_registros():
    for _ in range(2): otro_registro.agregar_persona(
        Cliente("Visitante", 30, Time(10, 0, 0), "00000000X"))
    global registro
    registro = registro + otro_registro
    print("Registros combinados.")

def menu():
    opciones = [
        "Introducir empleado",
        "Introducir cliente",
        "Buscar por nombre (y edad)",
        "Mostrar registro diario",
        "Mostrar empleados",
        "Visualizar persona por índice",
        "Combinar registros diarios",
        "Salir"
    ]
    while True:
        op = crear_menu(opciones)
        if op == 1: introducir_empleado()
        elif op == 2: introducir_cliente()
        elif op == 3: buscar_persona()
        elif op == 4: registro.visualizar_registro()
        elif op == 5: registro.visualizar_empleados()
        elif op == 6: visualizar_por_indice()
        elif op == 7: combinar_registros()
        elif op == 8: break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu()
