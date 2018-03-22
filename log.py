import csv
from datetime import datetime

def create_account():
    """Creates new instance of a Person class"""

    file = open('data.csv', 'a')
    writer = csv.writer(file)

    data = []
    print("What is your new login?>")
    login = input('>  ')
    #add a function that checks if the login is not taken

    print("What is your name?")
    name = input('>  ')

    print("What is your surname?")
    surname = input('>  ')

    print("what is your email?")
    email = input('>  ')

    #add a function that cheks if email is not taken
    print("What is you password?")
    password = input('> ')

    data.append(name)
    data.append(surname)
    data.append(login)
    data.append(password)
    data.append(email)

    writer.writerow(data)


def log_in():
    pass

def login_taken(login):
    """ Checks if the login in the base is already taken"""
    data_file = open('data.csv', 'r')
    # for person_data in data_file:
    #     try person_data[2] == login





create_account()
