import pandas as pd
exceldata1=pd.read_excel('..//data/Employee.xlsx',sheet_name="Sheet1")
print(exceldata1)
exceldata2=pd.read_excel('..//data/Employee.xlsx',sheet_name="Sheet2")
print(exceldata2)
exceldata5=pd.read_excel('..//data/Employee.xlsx',sheet_name="Sheet3")
print(exceldata5)
exceldata3=pd.concat([exceldata1,exceldata2],axis=1,join='inner')
print(exceldata3)
#exceldata4=pd.merge(left=exceldata1,rigth=exceldata2,how='inner')
#print(exceldata4)
print(exceldata1.compare(exceldata5))
print(exceldata1.to_html("demo.txt"))