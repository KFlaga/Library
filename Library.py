import csv
import librarian as lib
import log
import account as ac


def intro():
    """ Gives user possibility to either log in or to create account"""

    choice = 0
    while choice != '3':
        print("""
        LOGIN______________________________
        Welcome to the LIBRARY 6000 system!
        1 To log in
        2 To create a new account
        3 To exit

        For librarian acces enter 'admin'
            """
            )
        choice = input('>  ')

        if choice == '1':
            login, password = log.log_in()
            main_page(login, password)
        elif choice == '2':
            log.create_account()
        elif choice == '3':
            return
        elif choice == 'admin':
            librarian()
        else:
            print("Wrong comment, try again")

    print("Closing the system, goodbye")


def main_page(login, password):

    choice = '0'
    while choice != '5':
        print("""
        ACCOUNT_________________
        Welcome to your page
        What do you want to do?
        1. Search for a book
        2. Check your books
        3. Rent a book
        4. Change your account data
        5. Log out
            """
            )

        choice = input('>  ')
        if choice == '1':
            ac.search_for_books()
        elif choice == '2':
            ac.check_my_books(login)
        elif choice == '3':
            ac.rent_book(login)
        elif choice == '4':
            ac.change_account_details(login, password)
        elif choice == '5':
            print("LOGGING OUT")
            return
        else:
            print("Wrong command, try again")


def librarian():
    """Admins domain with access to admin funcitons """

    choice = 0
    while choice != '6':
        print("""\n
        ADMIN___________________________
        This is librairian account. What do you want to do?
        1. Return a book
        2. Add a book
        3. Delete a book
        4. Check person database
        5. Delete users account
        6. To quit
            """
            )
        choice = input('>  ')
        login = 0

        if choice is '1':
            print("Enter books code, to exit enter 'X':")
            ID = input('>  ')
            if ID == 'X':
                return
            lib.return_book(ID)
        elif choice is '2':
            lib.adding_books()
        elif choice is '3':
            lib.deleting_books()
        elif choice is '4':
            lib.person_search()
            while login != 'X':
                print("\n\nTo check users data enter his login, to exit enter 'X'\n")
                login = input('>  ')
                if login == '':
                    pass
                else:
                    lib.person_details(login) #add cheker if the login exists?
        elif choice is '5':
            while login != 'X':
                print("""
    Enter login of the user that you wish to delete,
    to exit enter 'X'
    Books borrowed by that person will be marked as returned!
                    """
                    )
                login = input('>  ')

                if login == '':
                    print("Enter an argument")
                if login == 'X':
                    return
                else:
                    books = []
                    ID_list = lib.person_rented(login)
                    if len(ID_list) == 0:
                        print("User doesnt exits!")
                    else:
                        for ID in ID_list:
                            lib.return_book(ID)
                    lib.delete_account(login)
        elif choice is '6':
            print('Goodbye!')
        else:
            print("Wrong command, try again")

intro()
