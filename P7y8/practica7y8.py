import json

# Excepciones personalizadas
class ErrorBiblioteca(Exception):
    def __init__(self, mensaje="Error en la biblioteca."):
        super().__init__(mensaje)

class ErrorArchivo(ErrorBiblioteca):
    def __init__(self, mensaje="Error al acceder al archivo."):
        super().__init__(mensaje)

# Clase base
class Publicacion:
    def __init__(self, titulo, autor, anio):
        if not titulo or not autor or not isinstance(anio, int) or anio <= 0:
            raise ErrorBiblioteca("Datos inválidos para publicación.")
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    @property
    def titulo(self): return self._titulo
    @property
    def autor(self): return self._autor
    @property
    def anio(self): return self._anio

    def descripcion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

# Clase derivada: Libro
class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        if not genero:
            raise ErrorBiblioteca("El género no puede estar vacío.")
        self._genero = genero

    @property
    def genero(self): return self._genero

    def descripcion(self):
        return f"[Libro] {super().descripcion()}, Género: {self.genero}"

# Clase derivada: Revista
class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        if not isinstance(num_edicion, int) or num_edicion <= 0:
            raise ErrorBiblioteca("Número de edición inválido.")
        self._num_edicion = num_edicion

    @property
    def num_edicion(self): return self._num_edicion

    def descripcion(self):
        return f"[Revista] {super().descripcion()}, Edición: {self.num_edicion}"

# Funciones de utilidad
def leer_cadena(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Entrada no válida.")

def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser un número entero positivo.")
        except ValueError:
            print("Introduce un número válido.")

def guardar_publicaciones(lista, nombre_archivo):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            datos = []
            for p in lista:
                if isinstance(p, Libro):
                    tipo = "Libro"
                    extra = {"genero": p.genero}
                elif isinstance(p, Revista):
                    tipo = "Revista"
                    extra = {"num_edicion": p.num_edicion}
                else:
                    continue
                datos.append({"tipo": tipo, "titulo": p.titulo, "autor": p.autor, "anio": p.anio, **extra})
            json.dump(datos, f, indent=4)
        print("Publicaciones guardadas correctamente.")
    except Exception:
        raise ErrorArchivo("No se pudo guardar el archivo.")

def cargar_publicaciones(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            lista = []
            for d in datos:
                if d["tipo"] == "Libro":
                    lista.append(Libro(d["titulo"], d["autor"], d["anio"], d["genero"]))
                elif d["tipo"] == "Revista":
                    lista.append(Revista(d["titulo"], d["autor"], d["anio"], d["num_edicion"]))
            print("Publicaciones cargadas correctamente.")
            return lista
    except FileNotFoundError:
        raise ErrorArchivo("El archivo no existe.")
    except Exception:
        raise ErrorArchivo("Error al leer el archivo.")

# Programa principal
def menu():
    publicaciones = []
    while True:
        print("\n--- Menú Biblioteca Digital ---")
        print("1. Añadir publicación")
        print("2. Mostrar publicaciones")
        print("3. Guardar publicaciones en archivo")
        print("4. Cargar publicaciones desde archivo")
        print("5. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            tipo = input("¿Libro o Revista? ").strip().lower()
            try:
                titulo = leer_cadena("Título: ")
                autor = leer_cadena("Autor: ")
                anio = leer_entero("Año: ")
                if tipo == "libro":
                    genero = leer_cadena("Género: ")
                    publicaciones.append(Libro(titulo, autor, anio, genero))
                elif tipo == "revista":
                    edicion = leer_entero("Número de edición: ")
                    publicaciones.append(Revista(titulo, autor, anio, edicion))
                else:
                    print("Tipo no válido.")
            except ErrorBiblioteca as e:
                print("Error:", e)

        elif opcion == "2":
            if publicaciones:
                for p in publicaciones:
                    print(p.descripcion())
            else:
                print("No hay publicaciones registradas.")

        elif opcion == "3":
            nombre = leer_cadena("Nombre del archivo para guardar: ")
            try:
                guardar_publicaciones(publicaciones, nombre)
            except ErrorArchivo as e:
                print("Error:", e)

        elif opcion == "4":
            nombre = leer_cadena("Nombre del archivo a cargar: ")
            try:
                publicaciones = cargar_publicaciones(nombre)
            except ErrorArchivo as e:
                print("Error:", e)

        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
