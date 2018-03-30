import csv
import time

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

def change_account_details():
    login = 'P.Gynt'
    password = '1234'

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
            change_name(login,password)
        elif change == '2':
            change_surname(login,password)
        elif change == '3':
            change_password(login,password)
        elif change =='4':
            return
        else:
            print("Error, wrong value")


    # change_name()
    # change_surname()
    # change_password()

def change_name(login,password):

    print("What is your new name?")
    new_name = input('>  ')
    print("Enter your password to accept the change")
    user_password = input('>  ')

    if user_password == password:
        with open('data.csv', 'r') as data_base_r:
            data_reader = csv.reader(data_base_r)

            # seearching for a line with inputed login
            with open("data.csv", 'r') as login_search:
                login_reader = csv.reader(login_search)
                next(login_reader)

                for lines in login_reader:
                    if lines[2] == login:
                        data_line = lines
                        break

            data_line[0] = new_name

            # find a way to print out the data to a new file with a
            # saving date as a name/header
            # Also find a way to read only the latest file for our readings

            with open('data1.csv', 'w') as data_base_w:
                data_writer = csv.writer(data_base_w)

                for line in data_reader:
                    if line[2] == login:
                        data_writer.writerow(data_line)
                        print(data_line)
                    else:
                        data_writer.writerow(line)
                        print(line)

def change_surname():
    pass

def change_password():
    pass

def date_namer():

    date = time.strftime("%Y-%m-%d %H:%M:%S")
    print(join(date,"USER DATA"))
    print(f"User Data {date}")

    #print(f"{num}.{genre}" for num, genre in book_type_translator.items())



date_namer()
#change_account_details()
