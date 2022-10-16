# """
# A simple, intuitive python library to access google spreadsheets
# through the Google Sheets API v4
# """
# import pygsheets


# # code taken from official pygsheets docs
# PATH = '/workspace/PP3_The_Coach/creds.json'
# gc = pygsheets.authorize(service_file=PATH)
# gc = pygsheets.authorize(service_account_file=PATH)
# sh = gc.open('players_data')  # Open GoogleSheet
# WK1 = sh[0]
# WK3 = sh[2]
# WK2 = sh[1]
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coach_data')

WK1 = SHEET.worksheet('player_start')
WK2 = SHEET.worksheet('users')
WK3 = SHEET.worksheet('final_data')


def insert_rows(my_list):
    """
    function that populates
    google sheet with players values
    """
    print('Please wait while your team is created')
    new_row = []
    num = 5
    i = 0
    while num > 0:
        each = my_list[i]
        new_row.append(each.name)
        new_row.append(each.age)
        new_row.append(each.height)
        new_row.append(each.weight)
        new_row.append(each.active_m_r)
        WK1.append_row(new_row)
        num -= 1
        new_row = []
        i += 1


# def insert_rows(my_list):
#     """
#     function that populates
#     google sheet with players values
#     """
#     print('Please wait while your team is created')
#     new_row = []
#     num = 5
#     my_row = 1
#     i = 0
#     while num > 0:
#         each = my_list[i]
#         new_row.append(each.name)
#         new_row.append(each.age)
#         new_row.append(each.height)
#         new_row.append(each.weight)
#         new_row.append(each.active_m_r)
#         WK1.insert_rows(row=my_row, number=1, values=new_row)
#         num -= 1
#         new_row = []
#         i += 1
#         my_row += 1


# def insert_rows2(my_list):
#     """
#     function that populates
#     google sheet with players values
#     """
#     new_row = []
#     num = 5
#     my_row = 1
#     i = 0
#     while num > 0:
#         each = my_list[i]
#         new_row.append(each.name)
#         new_row.append(each.train_value)
#         new_row.append(each.calorie_value)
#         new_row.append(each.nutrition_score)
#         WK3.insert_rows(row=my_row, number=1, values=new_row)
#         num -= 1
#         new_row = []
#         i += 1
#         my_row += 1


# def show_table1():
#     """
#     Making a table with starting player values
#     based on user inputs
#     """
#     first_table = WK1.range('A1:E6', returnas='matrix')
#     print(tabulate(first_table, headers="firstrow", tablefmt="fancy_grid"))


# def show_table2():
#     """
#     Making a table with final player values
#     based on user inputs and calculations
#     """
#     first_table = WK3.range('A1:D6', returnas='matrix')
#     print(tabulate(first_table, headers="firstrow", tablefmt="fancy_grid"))


# def user_score(val):
#     """
#     append or update users
#     team performance score in google spreadsheet
#     """
#     WK2.update_value("C1", val)


def insert_rows(my_list):
    """
    function that populates
    google sheet with players values
    """
    print('Please wait while your team is created')
    new_row = []
    num = 5
    i = 0
    while num > 0:
        each = my_list[i]
        new_row.append(each.name)
        new_row.append(each.age)
        new_row.append(each.height)
        new_row.append(each.weight)
        new_row.append(each.active_m_r)
        WK1.append_row(new_row)
        num -= 1
        new_row = []
        i += 1
       
# my_row = ['23223','ererer','rer']


# def insert_r(x):
#     for i in range(1,5):
#         WK1.append_row(x)


# insert_r(my_row)


# -------old code
# def insert_rows(my_list):
#     """
#     function that populates
#     google sheet with players values
#     """
#     print('Please wait while your team is created')
#     new_row = []
#     num = 5
#     my_row = 1
#     i = 0
#     while num > 0:
#         each = my_list[i]
#         new_row.append(each.name)
#         new_row.append(each.age)
#         new_row.append(each.height)
#         new_row.append(each.weight)
#         new_row.append(each.active_m_r)
#         WK1.insert_rows(row=my_row, number=1, values=new_row)
#         num -= 1
#         new_row = []
#         i += 1
#         my_row += 1
