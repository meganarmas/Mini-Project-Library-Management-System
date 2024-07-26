from Modules.user_operations import UserOperations
from Modules.authors_op import Authors
from Modules.books_op import Books_Op
from Modules.genres_op import GenreMenu


class LibraryManagement:

    def main():
        user_operations = UserOperations()
        authors_op = Authors()
        book_ops = Books_Op()
        genre_operations = GenreMenu()
        while True:
            print("Welcome to the Library Management System! \nMenu")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Enter choice: ")
            

            if choice == '1':
                book_ops.book_menu()
            elif choice == '2':
                user_operations.user_op_menu()
            elif choice == '3':
                authors_op.authors_menu()
            elif choice == '4':
                genre_operations.genre_main()
            elif choice == '5':
                print("Thank you for using the Library Management System! Now closing...")
                break
            else:
                print("Please enter a valid number.")

    if __name__ == "__main__":
        main()