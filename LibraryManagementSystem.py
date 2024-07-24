from Modules.user_operations import UserOperations
from Modules.authors_op import pass
from Modules.books_op import pass
from Modules.genres_op import pass

class LibraryManagement:
    def __init__(self, library):
        self.library = library

    def main(self):
        while True:
            print("Welcome to the Library Management System! \nMenu")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("What would you like to do?")

            if choice == '1':
                self.book_menu()
            elif choice == '2':
                self.user_op_menu()
            elif choice == '3':
                self.authors_menu()
            elif choice == '4':
                self.genre_menu()
            elif choice == '5':
                print("Thank you for using the Library Management System! Now closing...")
                break
            else:
                print("Please enter a valid number.")

    def book_menu(self):
            print("Book Operations Menu")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            choice = input("6. Enter choice: ")

            if choice == '1':
                self.add_book
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                pass
            else:
                print("Please enter a valid number.")
        
    def user_op_menu():
        print("Add a new user")
        print("2. View user details")
        print("3. Display all users")
        choice = input("Enter choice: ")

        if choice == '1':
            self.add_new_user()
        elif choice == '2':
            self.view_user()
        elif choice == '3':
            pass
        else:
            print("Please enter a valid number.")


    def authors_menu(self):
        print("Author Menu.")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        choice = input("4. Enter choice: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            print("Please enter a valid number.")

    def genre_menu(self):
        print("Genre Menu.")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        choice = input("4. Enter choice: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            print("Please enter a valid number.")


    if __name__ == "__main__":
        main()