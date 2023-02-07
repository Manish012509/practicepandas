from dataclasses import dataclass
from openpyxl import Workbook
@dataclass
class people():
    name:str
    number:int
    age:int=0
p=[people("Popie",12),people("Ramp",20),people("Konda",30,20)]
data=[[p.name,p.number,p.age]for p in p]
data=[['Name','Number','Age']]+data
print(data)  
w=Workbook()
sheet=w.active #sheet= is the name of the sheet
for i in data:
    sheet.append(i)
w.save("C:/Files/dataclass.xlsx")


