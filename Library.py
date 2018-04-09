import csv
import Librarian
import log
import account


""" Gives user possibility to either log in or to create account"""
    def intro():

        choice = 0
        while choise != '3':
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
                    login, password = log_in()
                    main_page(login, password)
                elif choice is '2':
                    create_account()
                else:
                    print("Wrong comment, try again")

        print("Closing the system, goodbye")


def main_page(login, password):

    choice = '0'
    while choice != '4':
        print("""
            Welcome to your page
            What do you want to do?
            1. Search for a book
            2. Check your books
            3. Change your account data
            4. Log out
            """
            )

            choice = input('>  ')
            if choice is '1':
                search_for_books()
            elif choice is '2':
                check_my_books()
            elif choice is '3':
                change_account_details(login, password)
            elif choice is '4':
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
