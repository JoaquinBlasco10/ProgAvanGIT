# user.py
class User:
    def __init__(self, name, user_id):
        self._name = name
        self._id = user_id
        self._borrowed_books = []

    @property
    def name(self): return self._name
    @property
    def user_id(self): return self._id
    @property
    def borrowed_books(self): return self._borrowed_books

    def borrow_book(self, isbn): self._borrowed_books.append(isbn)
    def return_book(self, isbn):
        if isbn in self._borrowed_books:
            self._borrowed_books.remove(isbn)

    def __str__(self):
        libros = ', '.join(self._borrowed_books) or "Ninguno"
        return f"{self._name} | ID: {self._id} | Libros prestados: {libros}"
