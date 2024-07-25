from classes.class_books import Def_Books

books = []

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
                    pass

                def borrow_books(self):
                    pass

                def return_books(self):
                    pass
                
                def search_book(self):
                    pass

                def display_books():
                    pass