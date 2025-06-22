class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
        pass

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# EBook subclass
class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size
        pass

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"

# PrintBook subclass
class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count
        pass

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library Class
class Library:
    def __init__(self):
        self.books = []

    # Add book method
    def add_book(self, book):
        self.books.append(book)

    # List books
    def list_books(self):
        for book in self.books:
            print(book)