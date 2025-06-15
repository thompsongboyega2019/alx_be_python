class Book:
    """Represents a book with a title, author, and check-out status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        self._books = []  # Private list of books

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True  # Success
        return False  # Book not found or not available

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True  # Success
        return False  # Book not found or wasn't checked out

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(book)
