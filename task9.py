filename = "BOOK.txt"

def create():
    author = input("Enter the author's last name: ")
    title = input("Enter the book title: ")
    publisher = input("Enter the publisher: ")
    year = input("Enter the publication year: ")
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
        print(f"Author: {author}, Title: {title}, Publisher: {publisher}, Year: {year}")

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
            author = input("Enter the new author's last name: ")
            new_title = input("Enter the new book title: ")
            publisher = input("Enter the new publisher: ")
            year = input("Enter the new publication year: ")
            books[i] = f"{author},{new_title},{publisher},{year}\n"
            break
    save(books)

while True:
    print("\nMenu:")
    print("1. Create database entry")
    print("2. Edit database entry")
    print("3. Delete entry")
    print("4. Search by criteria")
    print("5. View database")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book = create()
        with open(filename, "a") as file:
            file.write(book)
    elif choice == "2":
        title = input("Enter the book title to edit: ")
        edit(title)
    elif choice == "3":
        title = input("Enter the book title to delete: ")
        delete(title)
    elif choice == "4":
        criteria = int(input("Enter search criteria (0: author, 1: title, 2: publisher, 3: year): "))
        value = input("Enter value to search: ")
        results = search(criteria, value)
        for book in results:
            author, title, publisher, year = book.strip().split(',')
            print(f"Author: {author}, Title: {title}, Publisher: {publisher}, Year: {year}")
    elif choice == "5":
        view()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
