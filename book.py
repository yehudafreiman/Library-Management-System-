class Book:

    def __init__(self,title, author, isbn, is_available=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_available=is_available

    def __str__(self):
        print(f'book title: {self.title} author: {self.author} isbn: {self.isbn} is_available: {self.is_available}')
