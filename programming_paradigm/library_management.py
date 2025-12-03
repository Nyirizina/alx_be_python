class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Private attribute to track status
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_item(self):
        """Marks the book as available (returned)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        # Private list to store Book objects
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self):
        """Finds a book by title and returns it."""
        for book in self._books:
            if book.title == title:
                book.return_item()
                return True
        return False

    def list_available_books(self):
        """Prints all books that are currently not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")