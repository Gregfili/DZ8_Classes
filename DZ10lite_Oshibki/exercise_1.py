
def convert_to_int(value):
    try:
        result = int(value)
        print(f"Преобразование успешно: {result}")
    except ValueError:
        print("Ошибка: невозможно преобразовать значение в целое число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Попытка преобразования завершена.")

# Проверка
print("Тест 1: Преобразование строки '123'")
convert_to_int("123")

print("\nТест 2: Преобразование строки 'abc'")
convert_to_int("abc")

print("\nТест 3: Преобразование списка [1, 2, 3]")
convert_to_int([1, 2, 3])
