# cliente.py
from ficha import Ficha

class Cliente(Ficha):
    def __init__(self, nombre, edad, nacio, dni):
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self): return self._dni

    def visualizar(self):
        print(f"{self.nombre} | Edad: {self.edad} | Nacido: {self.nacio} | DNI: {self._dni}")

    def __eq__(self, otro):
        return isinstance(otro, Cliente) and self.nombre == otro.nombre and self.edad == otro.edad
