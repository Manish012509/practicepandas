from openpyxl import load_workbook
from openpyxl.drawing.image import Image

workbook=load_workbook(filename="C:/Files/demoopenxlwrite.xlsx")
sheet=workbook.active

logo=Image('../data/img.jfif')

logo.height=150
logo.width=150

sheet.add_image(logo,"D10")
workbook.save(filename='C:/Files/image1.xlsx')