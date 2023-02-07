from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference

workbook=Workbook()
sheet=workbook.active

rows=[
    ["Product","Online","Store"],
    [1,30,45],
    [2,40,30],
    [3,50,10],
    [4,60,40],
    [5,30,20],
    [6,10,70],
    [7,80,50]
]
for i in rows:
    sheet.append(i)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
workbook.save("C:/Files/Chart.xlsx")
