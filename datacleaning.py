import csv
from os import access
import pandas as pd
df = pd.read_csv('total_stars.csv')
data = []

print(df.columns)
df.drop(['Unnamed: 0','designation', 'Unnamed: 7', 'Star_name.1', 'Distance.1', 'Mass.1','Radius.1'],axis = 1, inplace = True)
print(df)
df.to_csv('main1.csv')