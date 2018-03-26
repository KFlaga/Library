

class Person():
    pass
# person is a database, nothing more than an account
# unless we will do it a class that will take out person data!
# And will call out persons books when needed
# There should be also an information for the librarian who has the book
# so that info should stay with the book?
# Book shouldn't have all its info in one file as it complicates
# adding books. There shoudl be corelated file that woudl keep that data
# and book should have

class Books(object):

    __init__(self,book):
        self.book = book
    # dectipts the csv file into data
    # add junction between books.csv and users holding the books
    # add multiple books of the same kind to the database and solve the
    # problems associated
    #

class Logging():
    """ Gives user possibility to either log in or to create account"""
    print("""Welcome to the LIBRARY 6000 system!
          1 To log in
          2 To create a new account
          3 To exit
          """
         )
    choice = input('>  ')

    while choise is not '3':
        if choice is '1':
            login = log_in() # login is users indicator
            Account(login)
        elif choice is '2':
            create_account()
        else:
            print("Wrong comment, try again")
    print("Closing the system, goodbye")
    

class Account():
    pass # add a small self.__init__ function to do sth


class Librarian():
    def adding_books():
        pass
    def deleting_books():
        pass
    def person_search():
        pass
    def delet_account():
        pass
