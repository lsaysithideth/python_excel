import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv',header=None)
df.columns = ['First','Last','Address','City','State','Area Code','Income']

to_drop(columns='Adress', inplace =True)

df = df.set_index('Area Code')

print(df.loc[8074])