
from library_manager import Library, generate_report

# Создаем экземпляр библиотеки
library = Library()

# Добавляем книги
library.add_book({'title': 'Master i Margarita', 'author': 'Mikhail Bulgakov', 'genre': 'Magical realism'})
library.add_book({'title': 'Voina i mir', 'author': 'Lev Tolstoi', 'genre': 'Epic novel'})

# Поиск книг
found_books = library.find_books(author='Fedor Dostoevskyi')
print("Найденные книги:", found_books)

# Генерация отчета
report = generate_report(library)
print(report)

# Удаление книги
library.remove_book('Idiot')

# Обновленный отчет
print(generate_report(library))

