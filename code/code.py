import pandas as pd
import numpy as np
df=pd.read_csv('../data/tested.csv')
#print(df)
'''
print(df.shape)#Print no of rows and coloums
print(df.isna().sum())#It will print all the sum of na values
df.drop(['Cabin'],axis=1,inplace=True)#It will delete the paticular row or values
df.fillna(method='ffill',inplace=True)#fill empty data with zeros way 1
df.fillna(0)
print(df)
print(df.isna().any())
print(df['Embarked'])#It categorize the data set to groups
#df['Survived']=df['Survived'].map{1:'yes',0:'no'}

'''
#print(pd.crosstab(index=df['Sex'],columns=df['Survived']))
#print(pd.pivot_table(df,index=['Sex','Age'],aggfunc=np.sum))
#print(df.sort_values(by=['Pclass','Age'],ascending=False))
df['Survived']=df['Survived'].apply(lambda val:'Yes' if val==1 else 'No')
print(df['Survived'])