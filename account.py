import csv

def search_for_books():
    """Ask for the type of search and then lists the books based of the criteria"""
    type_of_search = 0
    print("Do you want to search for books by the first letter of the title [A] or by the type [T]? ")
    while type_of_search is not 'X':
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
    print("What is the first letter of the searched title? Use bigcase")
    letter = input(">  ")
    with open('books.csv', 'r') as book_base:
        book_list = csv.reader(book_base)
        next(book_list)

        for line in book_list:
            if startswith(letter):
                print(line)
    return

def search_by_type():
    """Lists all books from the set type"""
    print("What type of book are you looking for? Enter a number \n1.fantasy\n2.crime\n3.adventure")

    book_type_number = 0

    while book_type_number != 'X'
        book_type_number = input('>  ')
        if book_type_number in book_type_translator:
            book_type = book_type_translator[book_type_number]
            with open('books.csv', 'r') as book_base:
                book_list = csv.reader(book_base)
                next(book_list)

                for line in book_list:
                    book_data = line.split(',')
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

def change_account_details():
    pass

def change_name():
    pass

def change_surname():
    pass

def change_password():
    pass

book_type_translator = {
    '1':'fantasy',
    '2':'crime',
    '3':'adventure'
    }
