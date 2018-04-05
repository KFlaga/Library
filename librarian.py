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


def deleting_books(kook_code):
    """ Deletes certain book from librairies, intakes books code"""

        """changes books data to 'rented' its 'return date' and by whom"""
        print("Which book do you wish to rent? Enter its code")
        book_code = input('>  ')
        book_code = 'A100' # temporary code, delete after finishing the function
        login = 'P.Gynt'
        with open('rented.csv', 'r') as rented_base:
            rented_reader = csv.reader(rented_base)
            next(rented_reader)

            # Verify if the book is available
            for line in rented_reader:
                print(line[-2])
                print("\n\n")
                if line[0] != book_code:
                    rented_book_data = line
                    change_books_status(login,book_code,rented_book_data)
                    break

        os.remove('rented.csv')
        os.rename('rented_temp.csv','rented.csv')




def person_search():
    pass


def delete_account():
    pass

adding_books()
