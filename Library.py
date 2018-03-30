import csv

class Person():
    pass
# person is a database, nothing more than an account
# unless we will do it a class that will take out person data!
# And will call out persons books when needed
# There should be also an information for the librarian who has the book
# so that info should stay with the book?
# Book shouldn't have all its info in one file as it complicates
# adding books. There should be corelated file that would keep that data
# and book should have

class Books(object):

    __init__(self,book):
        self.book = book
    # dectipts the csv file into data
    # add junction between books.csv and users holding the books
    # add multiple books of the same kind to the database and solve the
    # problems associated


class Logging(object):
    """ Gives user possibility to either log in or to create account"""
    def main():
        print("""
            Welcome to the LIBRARY 6000 system!
            1 To log in
            2 To create a new account
            3 To exit
            """
            )

        choice = input('>  ')

        while choise is not '3':
            if choice is '1':
                login = log_in() # login is users indicator
                Account.main(login)
            elif choice is '2':
                create_account()
            else:
                print("Wrong comment, try again")
        print("Closing the system, goodbye")


class Account(login):

    # long useless init for mt own amusement
    def __init__(self,login):
        self.login = login
        with open('data.csv','r') as data_file:
            data_list = csv.reader(data_file)
            for person_data in data_list:
                if self.login == person_data[2]:
                    self.name = person_data[0]
                    self.surname = person_data[1]
                    self.password = person_data[3]

        #call for person data

    def main_page():
        print("""
            Welcome to your page
            What do you want to do?
            1. Search for a book
            2. Check your books
            3. Change your account data
            4. Log out
            """
            )

        choice = '0'

        while choice is not '4':
            choice = input('>  ')
            if choice is '1':
                search_for_books()
            elif choice is '2':
                check_my_books()
            elif choice is '3':
                change_account_details(
                self.login
                self.password
                )
            else:
                print("Wrong command, try again")

        Logging.main()



class Librarian():
    def adding_books():
        pass
    def deleting_books():
        pass
    def person_search():
        pass
    def delete_account():
        pass
