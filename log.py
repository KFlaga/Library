import csv
from datetime import datetime

def create_account():
    """Adds person data into 'base.csv' """

    file = open('data.csv', 'a')
    writer = csv.writer(file)

    login_test = 1
    while login_test == 1:
        print("Welcome to the account creation!\nWhat is your new login?")
        login = input('>  ')
        login_test = login_taken(login)

    print("What is your name?")
    name = input('>  ')

    print("What is your surname?")
    surname = input('>  ')

    print("what is your email?")
    email = input('>  ')

    #add a function that cheks if email is not taken
    print("What is you password?")
    password = input('> ')

    data = []
    data.append(name)
    data.append(surname)
    data.append(login)
    data.append(password)
    data.append(email)

    writer.writerow(data)


def login_taken(login):
    """ Checks if the login in the base is already taken"""

    with open('data.csv', 'r') as data_file:
        data_list = csv.reader(data_file)
        next(data_list)

        for person_data in data_list:
            if login == person_data[2]:
                print("ERROR\nLOGIN TAKEN")
                return 1
    return 0

def log_in():
    """ Logs in the user into his accout"""
    print("Hello User! Enter your login or enter 1. to create account")
    check = 1
    while check == 1:
        login = input('>  ')
        if login == 1:
            create_account()
        print("Enter your password?")
        password = str(input('>  '))
        check_password(login,password)


def check_password(login, password):
    """Checks if the password and login are binded together"""

    with open('data.csv', 'r') as data_file:
        data_list = csv.reader(data_file)
        next(data_list)

        for person_data in data_list:
            if login == person_data[2]\
            and password == person_data[3]:
                print("WORKS FINE")
                return
        print(
        """Either password or Login is not good
        To create a new account enter '1'
        """
        )
        return 1



log_in()
