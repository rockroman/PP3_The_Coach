"""
A simple, intuitive python library to access google spreadsheets
through the Google Sheets API v4
"""
import pygsheets
from tabulate import tabulate
# code taken from official pygsheets docs
PATH = '//workspace//PP3_The_Coach//creds.json'
gc = pygsheets.authorize(service_account_file=PATH)
sh = gc.open('players_data')  # Open GoogleSheet
WK1 = sh[0]


def insert_rows(my_list):
    """
    function that populates
    google sheet with players values
    """
    new_row = []
    num = 2
    my_row = 1
    i = 0
    while num > 0:
        each = my_list[i]
        new_row.append(each.name)
        new_row.append(each.age)
        new_row.append(each.height)
        new_row.append(each.weight)
        new_row.append(each.active_m_r)
        WK1.insert_rows(row=my_row, number=1, values=new_row)
        num -= 1
        new_row = []
        i += 1
        my_row += 1


def show_table1():
    first_table = WK1.range('A1:E6', returnas='matrix')
    print(tabulate(first_table, headers="firstrow", tablefmt="fancy_grid"))

# make a variable that holds value of google sheet
# players values created by user input



# cell_range1 = WK1.range('A1:F6', returnas='matrix')

# WK1.insert_cols(5, number=1, values=['ACTIVE_met_rate'], inherit=False)
# WK1.delete_cols(5, number=1)
