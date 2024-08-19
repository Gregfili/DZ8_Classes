# utils/data_validation.py

def validate_book_data(data):
    """Проверяет, что данные книги корректны (имеются обязательные поля)."""
    required_fields = ['title', 'author', 'genre']
    for field in required_fields:
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            return False
    return True
