

class CMatFloat:
    def __init__(self):
        """Inicializa la matriz como None y las dimensiones en 0."""
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0

    def crear_matriz(self, nFilas, nColumnas):
        """Crea una matriz de ceros (1D o 2D) según los parámetros."""
        
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def crear_matriz_1d(self, nElementos):
        """Crea una matriz unidimensional de ceros."""
        self.crear_matriz(1, nElementos)

    def introducir_valores(self):
        """Permite al usuario introducir los valores en la matriz."""
        if not self.existe():
            print("La matriz no ha sido creada.")
            return
        
        print("Introduce los valores de la matriz:")
        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                self._Matriz[i, j] = leer_float(f"Elemento [{i}][{j}]: ")

    def mostrar_matriz(self):
        """Muestra la matriz actual si está creada."""
        if not self.existe():
            print("La matriz no ha sido creada.")
            return
        print("Matriz actual:")
        print(self._Matriz)

    def existe(self):
        """Verifica si la matriz está creada y no está vacía."""
        return self._Matriz is not None and self._Matriz.size > 0

    def sumar_matrices(self, otra_matriz):
        """Suma la matriz actual con otra matriz."""
        if not self.existe() or not otra_matriz.existe():
            print("Ambas matrices deben estar creadas.")
            return None
        if self._Matriz.shape != otra_matriz._Matriz.shape:
            print("Las matrices deben tener las mismas dimensiones.")
            return None
        return self._Matriz + otra_matriz._Matriz

    def restar_matrices(self, otra_matriz):
        """Resta la matriz actual con otra matriz."""
        if not self.existe() or not otra_matriz.existe():
            print("Ambas matrices deben estar creadas.")
            return None
        if self._Matriz.shape != otra_matriz._Matriz.shape:
            print("Las matrices deben tener las mismas dimensiones.")
            return None
        return self._Matriz - otra_matriz._Matriz

def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número decimal.")

def crear_menu(opciones_menu):
    print("\nMenú:")
    for i, opcion in enumerate(opciones_menu, start=1):
        print(f"{i}. {opcion}")
    return leer_int("Selecciona una opción: ")

def manejar_matrices(matriz):
    sub_opcion = crear_menu([
        "Sumar matrices",
        "Restar matrices",
        "Volver al menú principal"
    ])

    if sub_opcion == 1 or sub_opcion == 2:
        otra_matriz = CMatFloat()
        filas = leer_int("Introduce el número de filas para la segunda matriz: ")
        columnas = leer_int("Introduce el número de columnas para la segunda matriz: ")
        otra_matriz.crear_matriz(filas, columnas)
        print("Introduce los valores de la segunda matriz:")
        otra_matriz.introducir_valores()

        if sub_opcion == 1:
            resultado = matriz.sumar_matrices(otra_matriz)
            if resultado is not None:
                print("Resultado de la suma:")
                print(resultado)

        elif sub_opcion == 2:
            resultado = matriz.restar_matrices(otra_matriz)
            if resultado is not None:
                print("Resultado de la resta:")
                print(resultado)

def main():
    matriz = CMatFloat()
    while True:
        opcion = crear_menu([
            "Construir matriz 1D",
            "Construir matriz 2D",
            "Introducir matriz",
            "Mostrar matriz",
            "Operaciones con matrices",
            "Terminar"
        ])
        
        if opcion == 1:
            n_elementos = leer_int("Introduce el número de elementos para la matriz 1D: ")
            matriz.crear_matriz_1d(n_elementos)
            print("Matriz 1D creada.")

        elif opcion == 2:
            filas = leer_int("Introduce el número de filas: ")
            columnas = leer_int("Introduce el número de columnas: ")
            matriz.crear_matriz(filas, columnas)
            print("Matriz 2D creada.")

        elif opcion == 3:
            matriz.introducir_valores()

        elif opcion == 4:
            matriz.mostrar_matriz()

        elif opcion == 5:
            manejar_matrices(matriz)

        elif opcion == 6:
            print("Finalizando el programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecuta el programa principal
if __name__ == "__main__":
    main()
