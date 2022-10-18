from typing import List
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate


# code taken from love_sandwiches walk-through project
# by Code Institute
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


def insert_rows(my_list: List[str]) -> None:
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


def insert_rows2(my_list: List[str]) -> None:
    """
    function that populates
    google sheet with players values
    """
    new_row = []
    num = 5
    i = 0
    while num > 0:
        each = my_list[i]
        new_row.append(each.name)
        new_row.append(each.train_value)
        new_row.append(each.calorie_value)
        new_row.append(each.nutrition_score)
        WK3.append_row(new_row)
        num -= 1
        new_row = []
        i += 1


def show_table1() -> None:
    """
    Making a table with starting player values
    based on user inputs
    """
    first_table = WK1.get("A1:E6")
    print(tabulate(first_table, headers="firstrow", tablefmt="fancy_grid"))


def show_table2() -> None:
    """
    Making a table with final player values
    based on user inputs and calculations
    """
    first_table = WK3.get('A1:D6')
    print(tabulate(first_table, headers="firstrow", tablefmt="fancy_grid"))


def user_score(val: int) -> int:
    """
    append or update users
    team performance score in google spreadsheet
    """
    WK2.update("C1", val)
    return val
