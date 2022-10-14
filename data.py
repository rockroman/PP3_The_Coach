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
WK3 = sh[2]


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


def insert_rows2(my_list):
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
        new_row.append(each.train_value)
        new_row.append(each.calorie_value)
        new_row.append(each.nutrition_score)
        WK3.insert_rows(row=my_row, number=1, values=new_row)
        num -= 1
        new_row = []
        i += 1
        my_row += 1
   


def show_table1():
    first_table = WK1.range('A1:E6', returnas='matrix')
    print(tabulate(first_table, headers="firstrow", tablefmt="fancy_grid"))

def show_table2():
    first_table = WK3.range('A1:G6', returnas='matrix')
    print(tabulate(first_table, headers="firstrow", tablefmt="fancy_grid"))

red =['mik', 'po','ytyty', 'iuoiuoiu', 'uiuyiu']
# cell_range = WK1.range('F2:G7', returnas='matrix')
# WK1.update_values("F2:G7", values= red)
# make a variable that holds value of google sheet
# players values created by user input
# WK1.update_values

# WK1.update_values('F2:G2', [red])
# WK1.update_values('A2:B3', [['red'],['io']])

# cell_range1 = WK1.range('A1:F6', returnas='matrix')

# WK1.insert_cols(5, number=1, values=['ACTIVE_met_rate'], inherit=False)
# WK1.delete_cols(5, number=1)
# new_list = []
# def col_list(my_list):
    
#     for item in my_list:
#         new_item = [item]
#         new_list.append(new_item)

#     return new_list


# an = ['2', '4', 't', 'o']

# col_list(an)
