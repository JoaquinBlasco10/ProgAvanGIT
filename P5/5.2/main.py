# main.py
from book import Book
from library import Library
from user import User
from utils import crear_menu, generar_id, leer_int

def mostrar_enunciado():
    print("""
SISTEMA DE GESTIÓN DE BIBLIOTECA
Permite añadir/eliminar libros, registrar usuarios, prestar y devolver libros.
Todo estructurado en módulos con validación de entradas.
""")

biblioteca = Library()
usuarios = {}

def registrar_usuario():
    nombre = input("Nombre del usuario: ")
    uid = generar_id()
    usuarios[uid] = User(nombre, uid)
    print(f"Usuario registrado con ID: {uid}")

def añadir_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    libro = Book(titulo, autor, isbn)
    biblioteca.add_book(libro)
    print("Libro añadido.")

def eliminar_libro():
    isbn = input("ISBN a eliminar: ")
    print("Libro eliminado." if biblioteca.remove_book(isbn) else "Libro no encontrado.")

def realizar_prestamo():
    uid = input("ID del usuario: ")
    isbn = input("ISBN del libro: ")
    user = usuarios.get(uid)
    if user and biblioteca.lend_book(isbn):
        user.borrow_book(isbn)
        print("Préstamo realizado.")
    else:
        print("Error en el préstamo.")

def realizar_devolucion():
    uid = input("ID del usuario: ")
    isbn = input("ISBN del libro: ")
    user = usuarios.get(uid)
    if user and biblioteca.return_book(isbn):
        user.return_book(isbn)
        print("Devolución realizada.")
    else:
        print("Error en la devolución.")

def mostrar_libros():
    if biblioteca.books:
        for libro in biblioteca.books.values():
            print(libro)
    else:
        print("No hay libros.")

def menu():
    opciones = [
        "Añadir libro", "Eliminar libro", "Registrar usuario",
        "Realizar préstamo", "Realizar devolución", "Mostrar libros", "Salir"
    ]
    while True:
        op = crear_menu(opciones)
        if op == 1: añadir_libro()
        elif op == 2: eliminar_libro()
        elif op == 3: registrar_usuario()
        elif op == 4: realizar_prestamo()
        elif op == 5: realizar_devolucion()
        elif op == 6: mostrar_libros()
        elif op == 7:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    mostrar_enunciado()
    menu()
