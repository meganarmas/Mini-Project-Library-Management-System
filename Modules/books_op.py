from Modules.class_books import Def_Books

f = open('book_list.txt', 'r')

books_def = Def_Books

books = []
genres = []
authors = []


def book_menu():
    print("Book Operations Menu")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Enter choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        borrow_books()
    elif choice == '3':
        return_books()
    elif choice == '4':
        search_book()
    elif choice == '5':
        display_books()
    else:
        print("Please enter a valid number.")

def add_book():
    title = input("Add title of book: ")
    author = input("Add author of the book: ")
    isbn = input("Enter isbn: ")
    full_book = {'title': {title}, 'author': {author}, 'isbn': {isbn}}
    if len(books) >= 1:
        for book in books:
            if title in books.values():
                print(f"User {book} exists already.")
            else:
                books.append(full_book)
                print(f"{full_book} has been added")
    else:
        books.append(full_book)
        print(f"{full_book} has been added")

def borrow_books():
    title = input("Enter the title of a book you would like to borrow: ")
    if title not in books.index():
        print("Book was not found in library")
    else:
        print(f"{title} has been borrowed from the library.")

def return_books():
    found_book = input("Enter the ISBN of the book to be returned: ")
    found_book = [{entry["isbn"]: books.index(entry)} for entry in books]
    try:
        if len(found_book) > 1:
            print("Multiple books found.")
            for book in enumerate(found_book, start=1):
                print(f"{book.index()} found and returned")
    except ValueError:
        print("A book with that ISBN was not found.")
                    
def search_book():
    title = input("What is the name of the book you would like to find: ")
    book = title
    if book:
        print(f"Found {book} in the library!")
    else:
        print("Book with that title was not found.")

def display_books():
    if books:
            for book in books:
                print(book)
    else:
        print("No books found in the library.")