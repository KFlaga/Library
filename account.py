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
    return()

def search_by_type():
    pass

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
