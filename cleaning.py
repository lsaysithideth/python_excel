import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv',header=None)
df.columns = ['First','Last','Address','City','State','Area Code','Income']

df.drop(columns='Address', inplace =True)

df = df.set_index('Area Code')

df.First = df.First.str.split(expand=True)

df = df.replace(np.nan,'N/A',regex=True)

to_excel = df.to_excel('modified.xlsx')