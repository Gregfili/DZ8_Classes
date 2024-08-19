
def validate_user_input(data):
    if not isinstance(data, dict):
        raise TypeError("Ожидается словарь в качестве входных данных.")
    
    if "name" not in data or not isinstance(data["name"], str):
        raise ValueError("Отсутствует ключ 'name' или его значение не является строкой.")
    
    if "age" not in data or not isinstance(data["age"], int) or data["age"] <= 0:
        raise ValueError("Отсутствует ключ 'age' или его значение не является положительным числом.")
    
    print("Входные данные корректны.")

# Проверка
try:
    print("Тест 1: Корректные данные")
    validate_user_input({"name": "Alice", "age": 30})
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print("\nТест 2: Отсутствует ключ 'name'")
    validate_user_input({"age": 30})
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print("\nТест 3: Некорректное значение для 'age'")
    validate_user_input({"name": "Bob", "age": -5})
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print("\nТест 4: Некорректный тип входных данных")
    validate_user_input("Это не словарь")
except Exception as e:
    print(f"Ошибка: {e}")
