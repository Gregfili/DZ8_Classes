class UserAlreadyExistsError(Exception):
    """Исключение, выбрасываемое, если пользователь с данным именем уже существует."""
    pass

class UserNotFoundError(Exception):
    """Исключение, выбрасываемое, если пользователь с указанным именем не найден."""
    pass