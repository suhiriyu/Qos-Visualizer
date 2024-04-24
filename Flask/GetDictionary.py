
import openpyxl
workbook = openpyxl.load_workbook('input.xlsx')
sheet = workbook.active
    
data_dict = {}
for row in sheet.iter_rows(values_only=True):
        key = row[0]
        value = row[1]
        data_dict[key] = value 