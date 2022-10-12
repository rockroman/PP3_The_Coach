import re
from time import sleep
import sys
from email_validator import validate_email, EmailNotValidError
from data import sh


WK2 = sh[1]
USER_DATA = []

 
def display_menu():
    print("Hello and Welcome are you a New user?")
    status = input("press 'y' for yes and 'n' for no \n")
    if status == "y":
        new_user()   
    elif status == "n":
        exsisting_user()
       
 

def new_user():
    user_row = 1
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
    email = input("Please enter your email address: \n ")
    email_col = WK2.get_col(2)
    username_col = WK2.get_col(1)
    username_col_data = username_col[1:]
    email_col_data = email_col[1:]
    if (email in email_col_data):
        index = email_col_data.index(email)
        print(f"Welcome again {username_col_data[index]}")
    else:
        print('There is no such a user in database')
        display_menu()


def slow_print(item):
    """
    prints the message letter by letter
    with specified time delay
    """
    for char in item:
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(" ")
 



def welcome():
    """
    welcome message and a program description
    by using ASCII art 
    """
    line1 = "   Welcome to     "
    


def program_title():
    """
    prints title
    """

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