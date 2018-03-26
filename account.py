import csv
from datetime import datetime

def search_for_books():
    """Ask for the type of search and then lists the books based of the criteria"""
    type_of_search = 0
    while type_of_search is not 'X':
        print("Do you want to search for books by the first letter of the title [A]\n or by the type [T]? ")
        type_of_search = input(">  ")
        if type_of_search == 'A':
            search_by_letter()
        elif type_of_search == 'T':
            search_by_type()
        else:
            print("Command unknown, write 'A' or 'T', to exit type 'X'")
    return()

def search_by_letter():
    """ Lists books that are starting with the entered letter"""
    print("What is the first letter of the searched title? Use uppercase")
    letter = input(">  ")
    with open('books.csv', 'r') as book_base:
        book_list = csv.reader(book_base)
        next(book_list)

        for book_data in book_list:
            if book_data[0].startswith(letter):
                print(book_data)
    return

def search_by_type():
    book_type_translator = {
        '1':'fiction',
        '2':'crime',
        '3':'adventure'
    }

    """Lists all books from the set type"""
    print("What type of book are you looking for? Enter a number")
    print("\n".join(f"{num}.{genre}" for num, genre in book_type_translator.items()))

    book_type_number = 0

    while book_type_number != 'X':
        book_type_number = input('>  ')
        if book_type_number in book_type_translator:
            book_type = book_type_translator[book_type_number]
            with open('books.csv', 'r') as book_base:
                book_list = csv.reader(book_base)
                next(book_list)

                for book_data in book_list:
                    if book_data[-1] == book_type:
                        print(book_data)

        elif book_type_number is 'X':
            return
        else:
            print("Book type invalid, try again or [X] to exit")



def check_my_books():
    pass

def rent_book():
    pass

def change_account_details(name,surname,password):

    change = '0'
    while change is not '4':
        print("""
        What do you want to change?
        1. Name
        2. Surname
        3. Password
        4. To Exit
        """
        )
        change = input('>  ')

        if change == '1':
            change_name(password)
        elif change == '2':
            change_surname(password)
        elif change == '3':
            change_surname(password)
        elif change =='4'
            return
        else:
            print("Error, wrong value\n\n\")
    

def change_name():
    pass

def change_surname():
    pass

def change_password():
    pass


search_for_books()
