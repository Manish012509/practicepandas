import openpyxl

wb=openpyxl.load_workbook("C://Files/demoopenxlwrite.xlsx")
sheet=wb.active
sheet["A7"]="=SUM(A1:E1)"
wb.save("C://Files/newdemoopenxl.xlsx")