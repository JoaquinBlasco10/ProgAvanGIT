class Book:
    def __init__(self, title, author, isbn, status=False):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._status = status

    @property
    def title(self): return self._title
    @property
    def author(self): return self._author
    @property
    def isbn(self): return self._isbn
    @property
    def status(self): return self._status
    @status.setter
    def status(self, value): self._status = value

    def __str__(self):
        estado = "Prestado" if self._status else "Disponible"
        return f"{self._title} | {self._author} | ISBN: {self._isbn} | {estado}"
