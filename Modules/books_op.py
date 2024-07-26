from Modules.class_books import Def_Books
from Modules.genres_op import Genre_Class
from Modules.authors_op import Authors
from Modules.class_authors import Authors_Class


books = []
genres = []
authors = []

class Books_Op:
    def book_menu(self):
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

                def add_book(self):
                    title = input("Add title of book: ")
                    author = input("Add author of the book: ")
                    isbn = input("Enter isbn: ")
                    full_book = {'Title': {title}, 'Author': {author}, 'ISBN': {isbn}}

                def borrow_books(self):
                    title = input("Enter the title of a book you would like to borrow: ")
                    if title not in 

                def return_books(self):
                    pass
                
                def search_book(self):
                    searching_for_title = input("What is the name of the book you would like to find: ")

                def display_books():
                    for book in books:
                        print(f"Title: {book[name]}")