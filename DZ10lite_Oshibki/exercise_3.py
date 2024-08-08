
class NegativeNumberError(Exception):
    def __init__(self, number, message="Число отрицательное."):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (значение: {self.number})"

def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    print(f"Число {number} положительное.")

# Проверка
try:
    print("Тест 1: Положительное число 5")
    check_positive_number(5)
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

try:
    print("\nТест 2: Отрицательное число -10")
    check_positive_number(-10)
except NegativeNumberError as e:
    print(f"Ошибка: {e}")
