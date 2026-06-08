import pandas as pd

# df = pd.DataFrame({
#     'Team': ['CSK', 'MI', 'CSK', 'MI', 'RCB'],
#     'Runs': [100, 120, 150, 130, 110]
# })
# df_new=df.groupby('Team')['Runs'].sum()
# print(df_new)

df = pd.DataFrame({
    'Department':['IT','HR','IT','HR','IT'],
    'Salary':[50000,40000,70000,45000,60000]
})

new=df.groupby('Department')['Salary'].median()
df.head()
print(new)