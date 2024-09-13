
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Library:
    def __init__(self, list_of_books, name_of_library):
        self.list_of_books = list_of_books
        self.name_of_library = name_of_library
        self.lended_book=[]

    def display_book(self):
        for items in self.list_of_books:
             print(items)
        return "This are the books we have"
    def add_book(self, new_book):
         self.list_of_books.append(new_book.capitalize())
    def lend_book(self, book):
        if book in self.list_of_books:
            self.lended_book.append(book)
            self.list_of_books.remove(book)
            print("Book lending permission approved...")
        elif book in self.lended_book:
            print("Sorry the book is already been lended\n"
                  "Currently we only have these:- ")
            for items in self.list_of_books:
                print(items)
        else:
            print("Book's name entered is not available or name is wrong "
                  "and the available books are:- ")
            for items in self.list_of_books:
                print(items)


def system():
        Leo = Library(["Alphabets", "Gitanjali", "Ramayana", "Bornoporichoy","Mahabharat"], "Kid's library")
        user_name = input("Enter your name:- ")

        while True:
            try:

                user_input = eval(input(f"Welcome {user_name} to {Leo.name_of_library} \n"
                                        f"Enter (1) To display books we have\n"
                                        f"Enter (2) To donate a book \n"
                                        f"Enter (3) To Lend a book\n"
                                        f"Enter (4) To return a book\n"
                                        f"Enter (5) For exit"
                                        f":- "))
                x=[]
                if user_input == 1:
                    print(Leo.display_book())

                elif user_input == 2:
                    new_book = input("Enter name of book you want to donate:- ")
                    Leo.add_book(new_book.capitalize())
                    print( "Book has been added thank you for your donation")


                elif user_input == 3:
                    book = input("Enter the name of book you want to lend:- ")
                    Leo.lend_book(book.capitalize())
                    k=[book.capitalize(),user_name]
                    x.append(k)


                elif user_input == 4:
                    new_book = input("Enter the name of book you want to return:- ")
                    z=[new_book.capitalize(),user_name]
                    if z in x:
                        Leo.add_book(new_book.capitalize())
                        print("Thank you for returning book hope to se you soon")
                        x.remove(z)
                    else:
                        print("You did not lend this book")
                elif user_input == 5:
                    print(f"Thank you {user_name} for using our services")
                    break
                else:
                    print("Wrong input has been entered:- ")
            except:
                print("Error!!!")
system()
