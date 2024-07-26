from Modules.class_authors import Authors_Class

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
        author_name = input("Enter the author's name: ")
        biography = input ("Enter the author's biography: ")
        new_author = {'Name': {author_name}, 'Biography': {biography}}
        authors.append(new_author)
        print(f"{new_author} has been added to the library.")

    def view_details(self):
        name = input("Enter the author's name to search: ")
        found_name = [author for author in authors if Authors_Class.get_author().lower() == name.lower]
        if found_name in authors:
            try:
                print(f"{found_name} has been found.")
            except NameError:
                print("Author with that name has not been found.")
                    
    def display_authors(self):
        author = authors
        if author in Authors_Class.__author_name:
            print(author)
        else:
            print("No authors found.")