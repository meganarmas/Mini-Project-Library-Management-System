from classes.class_genres import Genre_Class

genres = []

class GenreMenu:
    def genre_main(self):
        print("Genre Menu.")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        choice = input("4. Enter choice: ")

        if choice == '1':
            add_new_genre()
        elif choice == '2':
            view_genres()
        elif choice == '3':
            display_genres()
        else:
            print("Please enter a valid number.")

            def add_new_genre():
                genre_name = input("Enter the new genre's name: ")
                genre_description = input ("Enter the description: ") 
                genre_category = input("Enter the genre category: ")
                exisiting_genre = get_genre_by

            def view_genres():
                for genre in Genre_Class:
                    if Genre_Class.get_name().lower() == name.lower():
                        return genre


            def display_genres():
                for genre in Genre_Class:
                    print(f"Name: {Genre_Class.get_name}, Description: {Genre_Class.get_description}, Category: {Genre_Class.get_category}")
                else:
                    print("Not available.")

