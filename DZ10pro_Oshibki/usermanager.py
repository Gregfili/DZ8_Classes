class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

class UserAlreadyExistsError(Exception):
    """Исключение, выбрасываемое, если пользователь с данным именем уже существует."""
    pass

class UserNotFoundError(Exception):
    """Исключение, выбрасываемое, если пользователь с указанным именем не найден."""
    pass

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