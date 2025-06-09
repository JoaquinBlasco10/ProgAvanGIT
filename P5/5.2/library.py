# library.py
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        return self.books.pop(isbn, None)

    def lend_book(self, isbn):
        book = self.books.get(isbn)
        if book and not book.status:
            book.status = True
            return True
        return False

    def return_book(self, isbn):
        book = self.books.get(isbn)
        if book and book.status:
            book.status = False
            return True
        return False

    def search_books(self, keyword):
        return [b for b in self.books.values()
                if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]
