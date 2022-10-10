# from data import sh
# import re

# WK2 = sh[1]
# USER_DATA = []

 
# def display_menu():
#     status = input("Hello are you a New user? y/n? \n")
#     if status == "y":
#         old_user()
#     elif status == "n":
#         new_user()
 

# def new_user():
#     while True:
#         username = input("PLease enter your username: \n ")
#         if not re.match(r'^[a-zA-z0-9]{2,12}$', username):
#             print(
#                     'userame must be 2 to 12 characters long and contain'
#                     'letters and numbers')
#             continue
#         break
#     while True:
#         email = input("Please enter your email address: \n ")
#         if not re.match(r'^[\w.-]+@[\w.-]{3,15}$', email):
#             print('email must be 3 to 15 characters long')  
#             continue
#         break



# try


    



















 
#     if create_login in users:
#         print("\nLogin name already exist!\n")
#     else:
#         create_passw = input("Create password: ")
#         users[createLogin] = create_passw
#         print("\nUser created\n")
 
# def old_user():
#     login = input("Enter login name: ")
#     passw = input("Enter password: ")
 
#     if login in users and users[login] == passw:
#         print("\nLogin successful!\n")
#     else:
#         print("\nUser doesn't exist or wrong password!\n")
 
# while status != "q":
#     displayMenu()