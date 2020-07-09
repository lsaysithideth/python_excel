import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv',header=None)
df.columns = ['First','Last','Address','City','State','Area Code','Area Code 2']

wanted_values = df[['First','Last','State']]
stored = wanted_values.to_excel('State_Location.xlsx',index=None)