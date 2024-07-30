from Modules.class_authors import Authors_Class

author_class = Authors_Class

authors = []


def authors_menu():
    print("Author Menu.")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("4. Enter choice: ")

    if choice == '1':
        add_new_author()
    elif choice == '2':
        view_details()
    elif choice == '3':
        display_authors()
    else:
        print("Please enter a valid number.")

def add_new_author():
    author_name = input("Enter the author's name: ")
    biography = input ("Enter the author's biography: ")
    new_author = {'name': {author_name}, 'biography': {biography}}
    if len(authors) >= 1:
        for author in authors:
            if author_name in author.values():
                print(f"User {author} exists already.")
            else:
                users.append(new_author)
                print(f"{author} has been added")
    else:
        authors.append(new_author)
        print(f"{new_author} has been added")

def view_details():
    name = input("Enter the author's name to search: ")
    found_name = [author for author in authors if author_class.get_author().lower() == name.lower]
    if found_name in authors:
        try:
            print(f"{found_name} has been found.")
        except NameError:
            print("Author with that name has not been found.")
                    
def display_authors():
    author = authors
    if author in author_class.__author_name:
        print(author)
    else:
        print("No authors found.")