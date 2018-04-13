import csv
from datetime import datetime

def create_account():
    """Adds person data into 'base.csv' """

    with open('data.csv', 'a', newline='') as data:
        data_writer = csv.writer(data)

        login_test = 1
        while login_test == 1: # Use True / False. Why do you even do this check if few lines below you return if login_test is 1
            print("""
            Welcome to the account creator!
            To exit at any time type 'X'"
            "What is your new login?
            """
            )
            login = input('>  ')
            login_test = login_taken(login)
            if login == 'X':
                return

            if login_test == 1:
                print('Unexpected problem, closing the creator!')
                return 1

            print("What is your name?")
            name = input('>  ')
            if name == 'X':
                return

            print("What is your surname?")
            surname = input('>  ')
            if surname == 'X':
                return

            # 4 lines below repeats 4 times - candidate for separate function
            print("what is your email?")
            email = input('>  ')
            if email == 'X':
                return

            #add a function that cheks if email is not taken
            print("What is you password?")
            password = input('> ')
            if password == 'X':
                return

            # Hahah, 'Congratulations' for making account, so pro achivement
            print("Congratulations,",name," you've created a new account!")

            # you could just write : data = [name, surname, login, password, email]
            data = []
            data.append(name)
            data.append(surname)
            data.append(login)
            data.append(password)
            data.append(email)

            data_writer.writerow(data)


# name this function: check_if_login_is_taken(login)
# then see that it makes descritpion needless
def login_taken(login):
    """ Checks if the login in the base is already taken"""
    
    # Use True / False for boolean conditions pls
    taken = 1
    while taken != 0: # for what do you need this loop?
        with open('data.csv', 'r') as data_file:
            data_list = csv.reader(data_file)
            next(data_list)

            for person_data in data_list:
                if person_data[2] is login:
                    print("ERROR\nLOGIN TAKEN")
                    
                    # Lol, how is it possible that taken == 'X'? There's no assignment
                    if taken == 'X':
                        return 1
                else:
                    taken = 0
    return 0


def log_in():
    """ After verification with 'data.csv' base returns users login"""

    print("Hello User! Enter your login OR enter '1' to create account")
    check = 2

    while check != 0: # Use True / False
        login = input('>  ')

        if login == '1':
            create_account()
            print("Enter your login again")
            login = input('>  ')

        print("Enter your password")
        password = str(input('>  ')) # is `str` needed here?
        check = check_password(login,password)

    return login, password


# For what do you need this description strings? Mostly they don't tell anything usefull
# except what is impled by function name already
# Rename it to: check_if_password_and_login_match()
# and name cleary states what this function does
def check_password(login, password):
    """Checks if the password and login are binded together"""

    with open('data.csv', 'r') as data_file:
        data_list = csv.reader(data_file)
        next(data_list)

        for person_data in data_list:
            if person_data[2] == login\
            and person_data[3] == password:
                print("WORKS FINE")
                return 0
    print(
    """Either password or Login is not good. Enter your login again.
    To create a new account enter '1'
    """
    )
    return 2 # Return True / False
