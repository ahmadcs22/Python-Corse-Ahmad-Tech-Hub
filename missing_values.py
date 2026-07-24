import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'Name': ['Ahmad', 'Ali', 'Anaya', 'Hania'],
#     'Marks': [90, np.nan, 85, np.nan]
# })
# df.dropna(axis=1,how='all',inplace=True)
# df.dropna(axis=1,thresh=3,inplace=True)
# df.dropna(axis=0,subset=['Marks'],inplace=True)
# df['Marks'].fillna(df['Marks'].mean())
# df.fillna(method='ffill')
# df.fillna(method='bfill')

df = pd.DataFrame({
    'Marks': [90, np.nan, 80]
})

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print(df)

