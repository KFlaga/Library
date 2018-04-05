import csv
import os
import datetime
from datetime import timedelta
from datetime import date

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


def check_my_books(login):
    """checks the books rented by the person in rented.csv base"""

    with open('rented.csv', 'r') as rented_base:
        rented_reader = csv.reader(rented_base)
        next(rented_reader)

        books_table = []

        #rented books[ID,rental_date,return_date,login]
        for line in rented_reader:
            if line[-1] == login:
                books_table.append([line[0],line[1],line[2]])

        print("Your rented books are:")

        with open('books.csv', 'r') as book_base:
            book_reader = csv.reader(book_base)
            for line in book_reader:
                for box in books_table:
                    if line[3] == box[0]:
                        print(line)
                        print("Rented on",box[1],"\nTo Be returned on",box[2])


def rent_book():
    """changes books data to 'rented' its 'return date' and by whom"""
    print("Which book do you wish to rent? Enter its code")
    book_code = input('>  ')

    with open('rented.csv', 'r') as rented_base:
        rented_reader = csv.reader(rented_base)
        next(rented_reader)

        # Verify if the book is available
        for line in rented_reader:
            print(line[-2])
            print("\n\n")
            if line[0] == book_code:
                if line[-2] == 'FALSE':
                    print('Books is unavailable')
                else:
                    rented_book_data = line
                    change_books_status(login,book_code,rented_book_data)
                    break

    os.remove('rented.csv')
    os.rename('rented_temp.csv','rented.csv')


def change_books_status(login, book_code,rented_book_data):
    """ creates rented_temp.csv file with changed book status"""

    # modifying book_data:
    rental_date = datetime.date.today()
    return_date = rental_date + timedelta(days= 40)

    rental_date = date.strftime(rental_date,'%d.%m.%Y')
    return_date = date.strftime(return_date,'%d.%m.%Y')

    new_rented_data = [book_code,
                    rental_date,
                    return_date,
                    'False',
                    login
                    ]

    with open('rented.csv', 'r') as rented_base_r:
        rented_reader = csv.reader(rented_base_r)

        with open('rented_temp.csv','w', newline = '') as rented_base_w:
            rented_writer = csv.writer(rented_base_w)

            for line in rented_reader:
                if line[0] == book_code:
                    rented_writer.writerow(new_rented_data)
                else:
                    rented_writer.writerow(line)


def change_account_details():
    """ Depending on the imput changes account details in 'data.csv'"""

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
            change_data(login,password,'name')
        elif change == '2':
            change_data(login,password,'surname')
        elif change == '3':
            change_data(login,password,'password')
        elif change =='4':
            return
        else:
            print("Error, wrong value")


def change_data(login,password,changed_data):

    changed_value = {
    'name':0,
    'surname':1,
    'password':3
    }

    #add an f string here
    print("What is your new",changed_data,"?")
    new_data = input('>  ')
    print("Enter your password to accept the change")
    user_password = input('>  ')

    #Out data base will be outdayed after the change
    #os.rename('data.csv','old_data.csv')

    if user_password == password:
        with open('data.csv', 'r') as data_base_r:
            data_reader = csv.reader(data_base_r)

            # searching for a line with inputed login
            data_line = []

            with open("data.csv", 'r') as login_search:
                login_reader = csv.reader(login_search)
                next(login_reader)

                for lines in login_reader:
                    if lines[2] == login:
                        data_line = lines
                        break

            # change the data
            data_line[changed_value[changed_data]] = new_data

            with open("data_temp.csv", 'w', newline='') as data_base_w:
                data_writer = csv.writer(data_base_w)

                for line in data_reader:
                    if line[2] == login:
                        data_writer.writerow(data_line)
                        print(data_line)
                    else:
                        data_writer.writerow(line)
                        print(line)

        os.remove('data.csv')
        os.rename('data_temp.csv','data.csv')

    else:
        print("Wrong password")
