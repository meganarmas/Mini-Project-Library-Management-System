from classes.class_authors import Authors_Class

authors = []

class Authors:
    def authors_menu(self):
        print("Author Menu.")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        choice = input("4. Enter choice: ")

        if choice == '1':
            self.add_new_author()
        elif choice == '2':
            self.view_details()
        elif choice == '3':
            self.display_authors()
        else:
            print("Please enter a valid number.")

    def add_new_author(self):
        pass

    def view_details(self):
        pass

    def display_authors():
        pass