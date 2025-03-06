filename = "BOOK.txt"

def create():
    author = input("Введіть прізвище автора: ")
    title = input("Введіть назву книги: ")
    publisher = input("Введіть видавництво: ")
    year = input("Введіть рік видання: ")
    return f"{author},{title},{publisher},{year}\n"

def load():
    with open(filename, "r") as file:
        return file.readlines()

def save(books):
    with open(filename, "w") as file:
        file.writelines(books)

def view():
    books = load()
    for book in books:
        author, title, publisher, year = book.strip().split(',')
        print(f"Автор: {author}, Назва: {title}, Видавництво: {publisher}, Рік: {year}")

def search(criteria, value):
    books = load()
    results = [book for book in books if value in book.strip().split(',')[criteria]]
    return results

def delete(title):
    books = load()
    books = [book for book in books if title not in book.strip().split(',')[1]]
    save(books)

def edit(title):
    books = load()
    for i, book in enumerate(books):
        if title in book.strip().split(',')[1]:
            author = input("Введіть прізвище нового автора: ")
            new_title = input("Введіть нову назву книги: ")
            publisher = input("Введіть нове видавництво: ")
            year = input("Введіть новий рік видання: ")
            books[i] = f"{author},{new_title},{publisher},{year}\n"
            break
    save(books)


while True:
    print("\nМеню:")
    print("1. Створити базу даних")
    print("2. Редагувати базу даних")
    print("3. Видалити запис")
    print("4. Пошук за критерієм")
    print("5. Переглянути базу даних")
    print("6. Вийти")
    choice = input("Введіть ваш вибір: ")
    if choice == "1":
        book = create()
        with open(filename, "a") as file:
            file.write(book)
    elif choice == "2":
        title = input("Введіть назву книги для редагування: ")
        edit(title)
    elif choice == "3":
        title = input("Введіть назву книги для видалення: ")
        delete(title)
    elif choice == "4":
        critery = int(input("Введіть критерій пошуку (0: автор, 1: назва, 2: видавництво, 3: рік): "))
        value = input("Введіть значення для пошуку: ")
        results = search(critery, value)
        for book in results:
            author, title, publisher, year = book.strip().split(',')
            print(f"Автор: {author}, Назва: {title}, Видавництво: {publisher}, Рік: {year}")
    elif choice == "5":
        view()
    elif choice == "6":
        break
    else:
        print("Невірний вибір. Будь ласка, спробуйте ще раз.")
