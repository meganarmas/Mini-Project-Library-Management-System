from Modules.user_operations import UserOperations
from Modules.authors_op import Authors
from Modules.books_op import Books_Op
from Modules.genres_op import GenreMenu

class LibraryManagement:

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
                Books_Op
            elif choice == '2':
                UserOperations
            elif choice == '3':
                Authors
            elif choice == '4':
                GenreMenu
            elif choice == '5':
                print("Thank you for using the Library Management System! Now closing...")
                break
            else:
                print("Please enter a valid number.")

    if __name__ == "__main__":
        main()