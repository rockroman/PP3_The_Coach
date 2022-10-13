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
    """
    Checks if the user email is in google spreadsheet
    (database) and if is retrieves username and greats the user
    if not promts the user back to menu
    """
    print("")
    email = input("Please enter your email address: \n ")
    email_col = WK2.get_col(2)
    username_col = WK2.get_col(1)
    username_col_data = username_col[1:]
    email_col_data = email_col[1:]
    if email in email_col_data:
        index = email_col_data.index(email)
        print('')
        print(f"Welcome Back {username_col_data[index]}")
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
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(" ")


# def welcome():
#     """
#     welcome message and a program description
#     by using ASCII art 
#     """
#     clrscr()
#     line1 = "   Welcome to     "
#     slow_print(line1)
#     program_title()
#     line2 = """
# Program that will determine performance
# percentage of the Team that you created
# 'The Coach' will give you a chance to create
# a Team of 5 Basketball players.
# You will:
# Assign each player with 3 training options
# Assign food intake with 3 options for a player
# The result will be  a percentage how well
# would your team perform based on your instructions
# ARE YOU READY?
#         """
#     # slow_print(line2)
#     print(line2)
#     time.sleep(1)
#     while True:
#         try:
#             answer = input("1)Proceed\n2)Exit program \n")
#             answer = int(answer)
#         except ValueError:
#             print("Please choose between 1 or 2")
#             continue
#         if answer > 2 or answer < 1:
#             print("Please choose between 1 or 2")
#             continue
#         break
#     if answer == 1:
#         display_menu()
#     elif answer == 2:
#         sys.exit()
   

def program_title():
    """
    prints title of programm
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



