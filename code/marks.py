import pandas as pd
import numpy as np
'''
class Record:
    def create_df(self):
        
        d1 = pd.read_csv('..//data/Marks.csv')
        #self.path=path
        #self.df=pd.DataFrame(self.path)
        #self.df['Total']=self.df['M1']+self.df['M2']+self.df['M3']+self.df['M4']+self.df['M5']+self.df['M6']
        #self.df['Total']=self
        d1=np.where(d1['M1']>=35 and d1['M2']>=35 and d1['M3']>=35 and d1['M4']>=35 and d1['M5']>=35 and d1['M6']>=35,True,False)

re=Record()
re.create_df()
        '''
class Rec:
    def create_table(self,path):
        self.path=path
        df=pd.read_csv(self.path)
        #print(df)
        df['Total']=df.iloc[:].sum(axis=1)
        df['avg']=df['Total']/5
        #print(df['Total'])
        #print(df['avg'])
        df['Rank']=df['avg'].rank()
        df['Result']=np.where((df['M1']>=35) &(df['M2']>=35) &(df['M3']>=35) & (df['M4']>=35) &(df['M5']>=35) &(df['M6']>=35 ),"Pass","Fail")
        print(df.sort_values(by=['Rank']))
'''
for i in df.iloc[:]:
    if int(i)>=35:
        print("Pass")
    else:
        print("Fail")
'''
obj=Rec()
obj.create_table('C:/Files/Marks.csv')

