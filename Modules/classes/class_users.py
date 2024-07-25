class UserClass:
    def __init__(self, first_name, last_name library_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__library_id = library_id
        self.__borrowed_books = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.__borrowed_books.append(book)
            return True
        
    def return_book(self, book):
        if book in self.__borrowed_books and book.return_book():
            self.__borrowed_books.remove(book)
            return True
        return False
    
    def detail(self):
        return f"First Name: {self.__first_name}, Last Name: {self.__last_name}, Library ID: {self.__library_id}, Borrowed Book: {[book.get_title() for book in self.__borrowed_books]}"
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_library_id(self):
        return self.__library_id
    
    def get_borrowed_books(self):
        return self.__borrowed_books
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    def get_library_id(self, library_id):
        self.__library_id = library_id
    
    def get_borrowed_books(self, borrowed_books):
        self.__borrowed_books = borrowed_books
