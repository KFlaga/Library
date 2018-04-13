import csv
import librarian as lib
import log
import account as ac


def intro():
    """ Gives user possibility to either log in or to create account"""

    # `if` ladders looks a bit ugly - almost always there's a better solution.
    # Apart from looking ugly they may be error-prone (maybe not in such small case) and
    # scales quite bad (e.g. adding new choices requires adding them in more than one place -
    # here its not a problem but sometimes those places may be in another file).
    # One easy idea may be creating dictionary of available options and handlers, like:
    # choices = {
    #    '1': log_and_go_to_main_page # -> extract each choice to separate function (remeber you can store function in variable)
    #    ...
    # }
    # Based on those dict not only you can dispatch work but also create message.
    # Again simplest way would be to store tuple (function, description) in `choices` dict
    # and for each entry (key, value) add `key + " " + value[1] + "\n".
    # There's only one caveat - dict is arbitrarily ordered, so you may consider
    # OrderedDict from collections module.
    # It may be my personal prefrence but I don't like raw tuples and even for simple
    # structures I prefer using namedtuple class from collections module.
    # With it you can create and access data using meaningful words, e.q.:
    #     Choice = collections.namedtuple('Choice', func, desc) 
    #     choices = { '1' : Choice(log_and_go_to_main_page, 'log in') }
    #     for (key, val) in choices : string_to_print += "{} {}\n".format(key, val.desc)
    # Ofc is such small program it may be a bit pedantic - but in larger if data is passed
    # around some files it often pays off.
    #
    # Actaully looking at structure of function from this file one could go even further and
    # make some factory class for them.
    # Lets define class Screen:
    # class Screen:
    #     def __init__(self, header, functions, descriptions)
    #          self.screen_text = header # e.q. LOGIN______________________________
    #                                    #      Welcome to the LIBRARY 6000 system!
    #          self.choices = {str(i): Choice(functions[i], descriptions[i]) for i in range(0, len(functions))}
    #          for (key, val) in self.choices:
    #              self.screen_text += "{} {}\n".format(key, val.desc)
    #
    #    def activate():
    #       ... # print screen_text ask and delegate work for given choice
    #
    # Screens for each of functions may be e.q. module level variables:
    # intro = Screen(...)
    # ...
    # intro.activate()
    #
    # GOOD HINT: always look for similarites in your code:
    #     - same code in many places (or very similar) -> e.g. extract to separate function if make sense
    #     - same layout of code (like here - funcs do similar stuff but with different data) -> make some generic
    #            representation for code and reuse it with different data
    
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
            # break ?
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
            
            # Extract to another function, this one is big enough - but whats more important
            # this function responsibility is to handle ADMIN main screen and preferably
            # each function should have one responsibility
            # If you would implement dict-based choices or sth similar it will come naturally:
            # handler will reside in separate function
            while login != 'X':
                print("\n\nTo check users data enter his login, to exit enter 'X'\n")
                login = input('>  ')
                if login == '':
                    pass
                else:
                    lib.person_details(login) #add cheker if the login exists?
        elif choice is '5':
            # extract to another function
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
