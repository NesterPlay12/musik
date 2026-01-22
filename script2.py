company = []


def add_staff(name, position):
    if name and position:
        company.append({"name": name, "position": position, "borrowed": False})
        return True
    else:
        return False

def borrow_book(title):
    for book in library:
        if book["title"] == title:
            if not book["borrowed"]:
                book["borrowed"] = True
                return "Книга выдана"
            else:
                return "Книга уже взята"
    return "Книга не найдена"

def return_book(title):
    for book in library:
        if book["title"] == title:
            if book["borrowed"]:
                book["borrowed"] = False
                return "Книга возвращена"
            else:
                return "Книга уже в библиотеке"
    return "Книга не найдена"

def show_staff():
    if not company:
        print("В штате нет сотрудников")
    else:
        for i, people in enumerate(company, 1):
            status = "взята" if people["borrowed"] else "доступна"
            print(f"{i}. {people['name']} - {people['position']} [{status}]")

def redactor_book():
    for book in library:
        if book["title"] == title:
            new_title = input("Новое название: ")
            new_author = input("Новый автор: ")

            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author

            print("Название изменено!")
            return
    print("Книга не найдена")

def delete_staff():
    for i, people in enumerate(company):
        if people["name"] == name:
            removed = company.pop(i)
            print(f"Удален сотрудник - {removed['name']}")
            return
    print("Сотрудник не найден")


if __name__ == "__main__":
    while True:
        print("\n1. Добавить сотрудника")
        print("\n2. Назначить оклад")
        print("\n3. Премии и штрафы")
        print("\n4. Показать штат")
        print("\n5. Редактировать должности")
        print("\n6. Уволить сотрудника")
        print("\n7. Выйти\n")

        choice = int(input("Выберите действие: "))

        if choice == 1:
            name = input("Имя: ")
            position = input("Должность: ")
            if add_book(name, position):
                print("Сотрудник добавлен")
            else:
                print("Ошибка: пустые поля")

        elif choice == 2:
            n = input("")
            print()

        elif choice == 3:
            n = input("")
            print()

        elif choice == 4:
            show_staff()

        elif choice == 5:
            title = input("Название книги: ")
            redactor_book()

        elif choice == 6:
            title = input("Название книги: ")
            delete_book()

        elif choice == 7:
            break

        else:
            print("Неверный выбор")
