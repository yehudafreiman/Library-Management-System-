from book import Book
from user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book:Book) -> str:
        self.list_of_books.append(book)
        return "-> The book successfully added to library"

    def add_user(self, user:User) -> str:
        self.list_of_users.append(user)
        return "-> The user successfully added to library"

    def borrow_book(self, user_id:str, book_isbn:str) -> str:
        for user in self.list_of_users:
            for book in self.list_of_books:
                if user_id == user.id and book_isbn == book.isbn and book.is_available:
                    user.borrowed_books.append(book)
                    book.is_available = False
                    return "-> The book has been borrowed successfully"
                else:
                    return "-> The book is borrowed or the user or book does not exist"

    def return_book(self, user_id:str, book_isbn:str) -> str:
        for user in self.list_of_users:
            for book in self.list_of_books:
                if user_id == user.id and book_isbn == book.isbn and not book.is_available:
                    user.borrowed_books.remove(book)
                    book.is_available = True
                    return "-> The book has been successfully returned"
                else:
                    return "-> The book is borrowed or the user or book does not exist"

    def list_available_books(self) -> str:
        available_books = []
        for book in self.list_of_books:
            if book.is_available:
                available_books.append(book.title)
        return f"-> available books: {available_books}"

    def search_book(self, key:str) -> str:
        result = []
        for book in self.list_of_books:
            if key in book.title or key in book.author:
                result.append(book.title)
        return f"-> search result: {result}"
