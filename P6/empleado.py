# empleado.py
from ficha import Ficha

class Empleado(Ficha):
    def __init__(self, nombre, edad, nacio, categoria, antiguedad):
        super().__init__(nombre, edad, nacio)
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self): return self._categoria
    @property
    def antiguedad(self): return self._antiguedad

    def visualizar(self):
        print(f"{self.nombre} | Edad: {self.edad} | Nacido: {self.nacio} | {self._categoria}, {self._antiguedad} años")
