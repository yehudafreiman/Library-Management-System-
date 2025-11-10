import demo_u, demo_b


class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book):
        self.list_of_books.append(book)
        print(f"{book} added to library books")

    def add_user(self, user):
        self.list_of_users.append(user)
        print(f"{user} added to library users")

    def borrow_book(self, book, user, user_id, book_isbn):
        if user_id in self.list_of_users:
            if book_isbn in self.list_of_books:
                user.borrowed_books.append(self.book)
                book.is_available = False
                print(f"{self.book} borrowed successfully to {self.user}")
            else:
                print("Book not found")
        else:
            print("User not found")

    def return_book(self, book, user, user_id, book_isbn):
        if user_id in self.list_of_users:
            if book_isbn in self.list_of_books:
                user.borrowed_books.remove(self.book)
                book.is_available = True
                print(f"{self.book} was successfully returned by {self.user}")
            else:
                print("Book not found")
        else:
            print("User not found")

    def list_available_books(self):
        available_books = []
        for book in self.list_of_books:
            if book.is_available:
                available_books.append(book)
        print("available books: ")
        return available_books

    def search_book(self, key):
        result = []
        for book in self.list_of_books:
            if book.title ==  key or book.author == key or book.isbn == key:
                result.append(book)
        print("search result: ")
        if len(result) == 0:
            print("The requested book was not found")
        print(result)


