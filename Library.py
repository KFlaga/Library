import csv
import librarian
import log
import account as ac


def intro():
    """ Gives user possibility to either log in or to create account"""

    choice = 0
    while choice != '3':
        print("""
        _____________________________________________________
            Welcome to the LIBRARY 6000 system!
            1 To log in
            2 To create a new account
            3 To exit
            """
            )
        choice = input('>  ')

        if choice is '1':
            login, password = log.log_in()
            main_page(login, password)
        elif choice is '2':
            log.create_account()
        elif choice is '3':
            return
        else:
            print("Wrong comment, try again")

    print("Closing the system, goodbye")


def main_page(login, password):

    choice = '0'
    while choice != '5':
        print("""
        _____________________________________________
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


class Librarian():
    def adding_books():
        pass
    def deleting_books():
        pass
    def person_search():
        pass
    def delete_account():
        pass

intro()
