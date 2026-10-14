from src.libtrack.services.auth_service import (
    authenticate,
    register_reader,
    register_librarian,
    create_default_admin
)


def login():
    print("\n=== Авторизация ===")

    login_value = input("Логин: ")
    password_value = input("Пароль: ")

    user = authenticate(login_value, password_value)

    if not user:
        print("\nНеверный логин или пароль")
        return None

    print(f"\nДобро пожаловать, {user.name} {user.surname}")
    return user


def register():
    print("\n=== Регистрация читателя ===")

    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")

    login_value = input("Логин: ")
    password_value = input("Пароль: ")

    try:
        register_reader(name, surname, patronymic, login_value, password_value)
        print("\nРегистрация успешна")
    except Exception as e:
        print(f"\nОшибка: {e}")


def register_librarian_ui():
    print("\n=== Регистрация библиотекаря ===")

    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")

    login_value = input("Логин: ")
    password_value = input("Пароль: ")

    try:
        register_librarian(name, surname, patronymic, login_value, password_value)
        print("\nБиблиотекарь создан")
    except Exception as e:
        print(f"\nОшибка: {e}")