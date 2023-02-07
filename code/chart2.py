from openpyxl import Workbook
from openpyxl.chart import *

workbook=Workbook()
sheet=workbook.active

rows=[
    ["Sl.n","Years","Sales"],
    [1,2010,10000],
    [2,2011,9000],
    [3,2012,20000],
    [4,2013,15000],
    [5,2014,12000],
    [6,2015,18000],
    [7,2016,25000]
]
for i in rows:
    sheet.append(i)
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=3,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
workbook.save("C:/Files/Chart2.xlsx")
