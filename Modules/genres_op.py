from Modules.class_genres import Genre_Class

genre_class = Genre_Class

genres = []

def genre_main():
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
    new_genre = {'Name': genre_name, 'Description': genre_description, 'Category': genre_category}
    if len(genres) >= 1:
        for genre in genres:
            if genre_name in genre.values():
                print(f"Genre {genre} exists already.")
            else:
                genres.append(new_genre)
                print(f"{new_genre} has been added")
    else:
        genres.append(new_genre)
        print(f"{new_genre} has been added")
                
def view_genres():
    for genre_name in genres:
        print(genre_name)
        

def display_genres():
    for genre_name in genre_class :
        print(f"Name: {genre_class.get_name}, Description: {genre_class.get_description}, Category: {genre_class.get_category}")
    else:
        print("Not available.")

