# utils/formatting.py

def format_book_data(data):
    """Форматирует данные книги для отчета."""
    return f"Title: {data.get('title')}, Author: {data.get('author')}, Genre: {data.get('genre')}"
