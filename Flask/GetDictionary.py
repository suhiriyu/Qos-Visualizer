import openpyxl
import openpyxl

def data_dictionary(choice1, choice2):
    workbook = openpyxl.load_workbook('input.xlsx')
    sheet = workbook.active

    if choice1 == 'catalyst9k' and choice2 == 'nexus9k':
        start = 1
        end = 28
    if choice1 == 'nexus9k' and choice2 == 'catalyst9k':
        start = 29
        end = 73
    
    data_dict = {}
    for idx, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if start <= idx <= end:
            key = row[0]
            value = row[1]
            data_dict[key] = value
    return data_dict