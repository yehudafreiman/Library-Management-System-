from book import Book
from user import User
from library import Library

if __name__ == "__main__":

    my_library = Library()

    is_running = True
    while is_running:
        print("Wellcome to The Lion Library!\nChoose from the menu:")
        print(" 1.add book\n 2.add user\n 3.borrow book\n 4.return book\n 5.get available books\n 6.search book\n 7.for exit")
        action = int(input("Enter here -> "))

        if action == 1: # add book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book isbn: ")
            my_library.add_book(Book(title, author, isbn))


        if action == 2: # add user
            name = input("Enter user name: ")
            user_id = input("Enter user id: ")
            my_library.add_user(User(name, user_id))

        if action == 3: # borrow_book
            user_id = input("Enter user id: ")
            book_isbn = input("Enter book isbn: ")
            my_library.borrow_book(user_id, book_isbn)

        if action == 4: # return_book
            user_id = input("Enter user id: ")
            book_isbn = input("Enter book isbn: ")
            my_library.return_book(user_id, book_isbn)

        if action == 5: # list available books
            Library.list_available_books(my_library)

        if action == 6: # search_book
            key = input("Enter book title/auther/isbn: ")
            my_library.search_book(key)

        if action == 7: # exit
            print("Goodbye!")
            is_running = False

