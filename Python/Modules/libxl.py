import openpyxl as xl


wb = xl.load_workbook("files.xlsx")
sheet = wb["Sheet1"]


sheet.column_dimensions["B"].width = 22
sheet.column_dimensions["G"].width = 20
sheet.column_dimensions["H"].width = 20
sheet.column_dimensions["J"].width = 35
sheet.column_dimensions["F"].width = 10


wb.save("last_files1.xlsx")
