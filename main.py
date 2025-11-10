from book import Book
from user import User
from library import Library

if __name__ == "__main__":

    my_library = Library()
    print("Wellcome to The Lion Library!")

    is_running = True
    while is_running:
        print()
        print("menu: ")
        print(" 1.add book\n 2.add user\n 3.borrow book\n 4.return book\n 5.get available books\n 6.search book\n 7.for exit")
        action = int(input("Enter a number: "))

        if action == 1: # add book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book isbn: ")
            print(my_library.add_book(Book(title, author, isbn)))

        if action == 2: # add user
            name = input("Enter user name: ")
            user_id = input("Enter user id: ")
            print(my_library.add_user(User(name, user_id)))

        if action == 3: # borrow book
            book_isbn = input("Enter book isbn: ")
            user_id = input("Enter user id: ")
            print(my_library.borrow_book(user_id, book_isbn))

        if action == 4: # return book
            book_isbn = input("Enter book isbn: ")
            user_id = input("Enter user id: ")
            print(my_library.return_book(user_id, book_isbn))

        if action == 5: # list available books
            print(my_library.list_available_books())

        if action == 6: # search book
            key = input("Enter some letters from title author to search: ")
            print(my_library.search_book(key))

        if action == 7: # exit
            print("Goodbye!")
            is_running = False
