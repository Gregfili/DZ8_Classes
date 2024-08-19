# catalog.py

from library_manager.utils.data_validation import validate_book_data

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_data):
        """Добавляет книгу в библиотеку, если данные корректны."""
        if validate_book_data(book_data):
            self.books.append(book_data)
        else:
            raise ValueError("Некорректные данные книги.")

    def remove_book(self, title):
        """Удаляет книгу из библиотеки по названию."""
        self.books = [book for book in self.books if book.get('title') != title]

    def find_books(self, title=None, author=None, genre=None):
        """Ищет книги по названию, автору или жанру."""
        result = self.books
        if title:
            result = [book for book in result if book.get('title') == title]
        if author:
            result = [book for book in result if book.get('author') == author]
        if genre:
            result = [book for book in result if book.get('genre') == genre]
        return result

    def view_all_books(self):
        """Возвращает список всех книг в библиотеке."""
        return self.books
