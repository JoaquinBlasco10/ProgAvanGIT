# registro.py
from empleado import Empleado
from cliente import Cliente

class RegistroDiario:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, p):
        if isinstance(p, (Empleado, Cliente)):
            self._personas.append(p)

    def visualizar_registro(self):
        for p in self._personas: p.visualizar()

    def visualizar_empleados(self):
        for p in self._personas:
            if isinstance(p, Empleado): p.visualizar()

    def es_empleado(self, p):
        return isinstance(p, Empleado)

    def __getitem__(self, i):
        return self._personas[i]

    def __add__(self, otro):
        nuevo = RegistroDiario()
        nuevo._personas = self._personas + otro._personas
        return nuevo
