from Modules.class_genres import Genre_Class

genre_class = Genre_Class

genres = []

class GenreMenu:
    def genre_main(self):
        print("Genre Menu.")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        choice = input("4. Enter choice: ")

        if choice == '1':
            self.add_new_genre()
        elif choice == '2':
            self.view_genres()
        elif choice == '3':
            self.display_genres()
        else:
            print("Please enter a valid number.")

    def add_new_genre():
        genre_name = input("Enter the new genre's name: ")
        genre_description = input ("Enter the description: ") 
        genre_category = input("Enter the genre category: ")
        new_genre = {'Name': {genre_name}, 'Description': {genre_description}, 'Category': {genre_category}}
        if genre_name in genre_class.get_name:
            exisiting_genre = genre_class.get_name(genre_name)
            print(f"Genre {exisiting_genre} exists already.")
        else:
            genres.append(new_genre)
            print(f"{new_genre} has been added")
                
    def view_genres(self):
        for genre_name in genre_class:
            if genre_class.get_name().lower() == genre_name.lower():
                print(genre_name.lower())

    def display_genres(self):
        for genre_name in genre_class :
            print(f"Name: {genre_class.get_name}, Description: {genre_class.get_description}, Category: {genre_class.get_category}")
        else:
            print("Not available.")

