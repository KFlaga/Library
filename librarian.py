import csv


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

    books_table = [title, author, year, new_code, book_type]

    # rented_table = [ID,rental_date,return_date,RETURNED,login]
    rented_table = [new_code,,,'TRUE',login]

    
    # morifier of booth books.csv and rented.csv files


def deleting_books():
    pass


def person_search():
    pass


def delete_account():
    pass

adding_books()
