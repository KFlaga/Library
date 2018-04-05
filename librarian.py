import csv
import os


def adding_books():
    """ Adds books to database and then sorts the bookbase by code"""

    book_type_translator = {
                            '1':'fiction',
                            '2':'crime',
                            '3':'adventure'
                            }
    book_type_translator_letter = {
                                '1':'F',
                                '2':'C',
                                '3':'A'
                                }

    print("""What type of a book do you wish to add? To exit type 'x'""")
    print("\n".join(f"{num}.{genre}" for num,
     genre in book_type_translator.items()))

    type = 0
    stoper = 0

    # Creating new books ID (its type as the last one in the base)
    while stoper == 0:
        type = input('>  ')
        if type == '1' or type == '2' or type == '3':
            stoper = 1
        elif type == 'x':
            return
        else:
            print("Invalid number, try again")

    book_type = book_type_translator[type]

    with open('rented.csv','r') as book_base:
        book_rented = csv.reader(book_base)

        for line in book_rented:
            if line[0].startswith(book_type_translator_letter[type]):
                code_letter = line[0]

    code_number = int(code_letter[1:])
    code_number +=1
    code_number = str(code_number)
    new_code = ''.join([code_letter[0],code_number])



    print("What is the books title?")
    title = input('>  ')

    print("Who is the author?")
    author = input('>  ')

    print('What is the year the books has been published?')
    year = int(input('>  '))

    new_book = [title, author, year, new_code, book_type]
    # rented_table = [ID,rental_date,return_date,RETURNED,login]
    new_rented = [new_code,0,0,'TRUE',0]

    # morifier of booth books.csv and rented.csv files
    with open('books.csv', 'a') as book_base:
        book_appender = csv.writer(book_base)
        book_appender.writerow(new_book)

    with open('rented.csv', 'a') as rented_base:
        rented_appender = csv.writer(rented_base)
        rented_appender.writerow(new_rented)


def deleting_books():
    book_code = "A101"
    """ Deletes certain book from librairies, intakes books code"""

    print("Which book do you wish to rent? Enter its code")

    with open('rented.csv', 'r', newline='') as rented_base_r:
        rented_reader = csv.reader(rented_base_r)

        with open('rented_temp.csv','w',newline='') as rented_base_w:
            rented_writer = csv.writer(rented_base_w)

# rented.csv = [book_code,rental_date,return_date,RETURNED,login ]
            for line in rented_reader:
                if line[0] != book_code:
                    rented_writer.writerow(line)

    with open('books.csv', 'r', newline='') as book_base_r:
        book_reader = csv.reader(book_base_r)

        with open('books_temp.csv', 'w', newline='') as book_base_w:
            book_writer = csv.writer(book_base_w)

            for row in book_reader:
                if row[3] != book_code:
                    book_writer.writerow(row)



    os.remove('rented.csv')
    os.rename('rented_temp.csv','rented.csv')

    os.remove('books.csv')
    os.rename('books_temp.csv','books.csv')



def person_search():
    pass


def delete_account():
    pass

deleting_books()
