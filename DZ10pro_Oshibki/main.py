# Определяем класс User
class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"User(username={self.username}, email={self.email}, age={self.age})"

# Определяем пользовательские исключения
class UserAlreadyExistsError(Exception):
    """Исключение, выбрасываемое, если пользователь с данным именем уже существует."""
    pass

class UserNotFoundError(Exception):
    """Исключение, выбрасываемое, если пользователь с указанным именем не найден."""
    pass

# Определяем класс UserManager
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        """Добавляет пользователя в словарь."""
        if user.username in self.users:
            raise UserAlreadyExistsError(f"Пользователь с именем {user.username} уже существует.")
        self.users[user.username] = user
        print(f"Пользователь {user.username} успешно добавлен.")

    def remove_user(self, username: str):
        """Удаляет пользователя из словаря."""
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем {username} не найден.")
        del self.users[username]
        print(f"Пользователь {username} успешно удален.")

    def find_user(self, username: str) -> User:
        """Возвращает пользователя по имени."""
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем {username} не найден.")
        return self.users[username]

# Основная функция программы
def main():
    manager = UserManager()

    # Добавим пользователей
    try:
        user1 = User("ivan_petrov", "ipetrov@example.ru", 45)
        manager.add_user(user1)

        user2 = User("alex_karelin", "akarelin@example.ru", 29)
        manager.add_user(user2)

        # Попробуем добавить пользователя с тем же именем
        manager.add_user(user1)
    except UserAlreadyExistsError as e:
        print(e)

    # Попробуем удалить пользователя
    try:
        manager.remove_user("alex_karelin")
        
        # Попробуем удалить пользователя, которого нет в словаре
        manager.remove_user("sergei")
    except UserNotFoundError as e:
        print(e)

    # Попробуем найти пользователей
    try:
        user = manager.find_user("ivan_petrov")
        print(user)
        
        # Попробуем найти пользователя, которого нет в словаре
        user = manager.find_user("sergei")
    except UserNotFoundError as e:
        print(e)

# Запуск основной программы
if __name__ == "__main__":
    main()
