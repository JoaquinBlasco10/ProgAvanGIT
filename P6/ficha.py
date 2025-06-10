# ficha.py
from time import Time

class Ficha:
    def __init__(self, nombre="", edad=0, nacio=None):
        self._nombre = nombre
        self._edad = edad
        self._nacio = nacio if nacio else Time(0, 0, 0)

    @property
    def nombre(self): return self._nombre
    @property
    def edad(self): return self._edad
    @property
    def nacio(self): return self._nacio

    def visualizar(self):
        print(f"{self._nombre}, Edad: {self._edad}, Nacido a las: {self._nacio}")
