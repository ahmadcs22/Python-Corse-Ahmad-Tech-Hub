# import pandas as pd 

# df = pd.read_csv('Ecommerce_Purchases.csv')

# print(df)
# print(df.head()) 5 row 14 coloms
# print(df.shape) 10k / 14
# print(df['Purchase Price'].mean()) 50 
# print(df['Purchase Price'].max())99
# print(df['Purchase Price'].min())0
# print(df[df['Language']=='en'].shape[0])1098
# print(df[df['Job']=='Lawyer'].shape[0]) 30
# print(df[df['AM or PM']=='AM'].shape[0]) 3932
# print(df.shape[0]-df[df['AM or PM']=='AM'].shape[0]) 5068
# print(df.shape) 10k
# print(df['Job'].value_counts().head(5))
# print(df.loc[df['Lot']=='90 WT','Purchase Price'].values[0])
# print(df.loc[df['Credit Card']== 30246200000000,'Email'].values[0])
# print(df[(df['CC Provider']== 'American Express') & (df['Purchase Price'] >95)].shape[0])
# print((df['CC Exp Date'].str.split('-').str[2]=='22').sum())
# print(df['Email'].str.split('@').str[1].value_counts().head(5))
# ---------------------


import pandas as pd 

df = pd.read_csv('Ecommerce_Purchases.csv')

# print(df.head())
# print(df.shape[1])
# print(df.shape)
# print(df['Purchase Price'].mean())
# print(df['Purchase Price'].max())
# print(df['Purchase Price'].min())
# print(df[df['Language']=='en'].shape[0])
# print(df[df['Job']== 'Lawyer'].shape[0])
# print(df[df['AM or PM']== 'AM'].shape[0])
# print(df[df['AM or PM']== 'PM'].shape[0])
# print(df['Job'].value_counts().head(5))
# print(df.loc[ df['Lot']== '90 WT',"Purchase Price"].values[0])
# print(df.loc[df['Credit Card']== 6011580000000000,"Email"].values[0])
# print(df[(df["CC Provider"]== "American Express") & (df["Purchase Price"] > 95)].shape[0])
# print((df['CC Exp Date'].str.split('-').str[2] == '22').sum())
# print((df['Email'].str.split('@').str[1].value_counts().head(5)))

# ------