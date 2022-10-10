"""
A simple, intuitive python library to access google spreadsheets
through the Google Sheets API v4
"""
import pygsheets

# code taken from official pygsheets docs
# PATH = 'C:\\Users\\una&roman\\OneDrive\\Radna površina\\test.py\\creds.json'
PATH = '/workspace/PP3_The_Coach/creds.json'
gc = pygsheets.authorize(service_account_file=PATH)
sh = gc.open('players_data')  # Open GoogleSheet
WK1 = sh[0]
# cell_range = WK1.range('A1:E3', returnas='matrix')  
# print(cell_range)  


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
