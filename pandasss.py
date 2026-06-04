import numpy as np
import pandas as pd 


# # label = ['ahmad','ali','anaya','hania']
# # arr=[90,91,92,92]
# # datag=np.array([12,20,22,45])
# # di = {
# #     'a': 11,
# #     'b': 22,
# #     'c': 33,
# #     'd': 44
# # }

# # hi= pd.Series(arr,di)
# # print(hi)

# series1 = pd.Series([1,2,3,4,5],index=['psl','ipl','bbl','ilt20','cpl'])

# series2=pd.Series([1,2,3,6,5],index=['psl','ipl','bbl','BBB','cpl'] )


# print(series1+series2)

# np.random.seed(101)

# df = pd.DataFrame(
#     np.random.rand(5, 4),
#     index="A B C D E".split(),
#     columns="V W X Y".split()
# )
# # df['new']= df['V']+ df['W']
# # df.drop('new',axis=1)
# # df.drop(index='E', inplace=True)
# print(df)


data = {
    'name' : ['ahmad','ali','anaya'],
    'grades': ['A','B','C']
}

# df = pd.DataFrame(data)

# df['lable']= ['97','98','99']
# df.set_index('lable',drop=False)
# df=df.reset_index()
# df.drop('index',index= 1,inplace=True)

# df=df.set_index('lable')
# df=df.reset_index()
# df.drop('lable',axis=1,inplace=True)
# df = df[df['grades'] == 'A']   
# print(df)
# print(df.loc['97'])
# print(df.loc['97':'99',['name']])
# print(df.iloc[0:3, 0:1])


df = pd.DataFrame({
    'Name': ['Ahmad','Ali','Anaya'],
    'Marks': [90,80,95]
})

df['Result'] = df['Marks'] > 85

print(df)