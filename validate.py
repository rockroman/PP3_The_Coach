import re
from time import sleep
import time
import sys
from email_validator import validate_email, EmailNotValidError
from data import sh
from run import clrscr


WK2 = sh[1]
USER_DATA = []


def display_menu():
    """
    Start menu that directs the user wether
    a new or existing option is chosen 
    """
    clrscr()
    program_title()
    print("Hello and Welcome are you: \n")
    status = input("a)New User\nb)Exsisting user \n")
    while status not in ("a", "b"):
        print("Please choose between a or b")
        status = input("a)New User\nb)Exsisting user \n")
    if status == "a":
        new_user()
    elif status == "b":
        exsisting_user()
       
 
def new_user():
    """
    Creating a new user based on username and 
    email, validating that inputs are within parameters
    and moving the new user data into (database)
    google spreadsheet
    """
    user_row = 0
    while True:
        username = input("Please enter your username: \n ")
        if not re.match(r'^[a-zA-z0-9]{2,12}$', username):
            print(
                    'userame must be 2 to 12 characters long and contain'
                    'letters and numbers')
            continue
        break
    while True:
        try:
            email = input("Please enter your email address: \n ")
            validate_email(email)
        except EmailNotValidError as err:
            print(str(err))
            continue
        break
    WK2.insert_rows(row=user_row, number=1, values=[username, email])
    user_row += 1
    

def exsisting_user():
    """
    Checks if the user email is in google spreadsheet
    (database) and if is retrieves username and greats the user
    if not promts the user back to menu
    """
    print("")
    email = input("Please enter your email address: \n ")
    email_col = WK2.get_col(2)
    username_col = WK2.get_col(1)
    user_score_col = WK2.get_col(3)
    username_col_data = username_col[0:]
    email_col_data = email_col[0:]
    user_score_col_data = user_score_col[0:]
    if email in email_col_data:
        index = email_col_data.index(email)
        print('')
        print(f"Welcome Back {username_col_data[index]}")
        print(f"Your team percentage last time \
was {user_score_col_data[index]}")
        time.sleep(2)
    else:
        print('There is no such a user in database')
        time.sleep(1.5)
        display_menu()


def slow_print(item):
    """
    prints the message letter by letter
    with specified time delay
    """
    for char in item:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(" ")
   

def program_title():
    """
    prints title of programm
    """
    clrscr()
    print('                                  ')
    print('         ████████╗██╗  ██╗███████╗')
    print('         ╚══██╔══╝██║  ██║██╔════╝')
    print('            ██║   ███████║█████╗  ')
    print('            ██║   ██╔══██║██╔══╝  ')
    print('            ██║   ██║  ██║███████╗')
    print('            ╚═╝   ╚═╝  ╚═╝╚══════╝')
    print('                                           ')
    print('  ██████╗  ██████╗   █████╗  ██████╗ ██╗  ██╗')
    print(' ██╔════╝ ██╔═══██╗ ██╔══██╗██╔════╝ ██║  ██║')
    print(' ██║      ██║   ██║ ███████║██║      ███████║')
    print(' ██║      ██║   ██║ ██╔══██║██║      ██╔══██║')
    print(' ╚██████╗ ╚██████╔╝ ██║  ██║╚██████╗ ██║  ██║')
    print('  ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝')


