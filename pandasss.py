import numpy as np
import pandas as pd 

# label = ['ahmad','ali','anaya','hania']
# arr=[90,91,92,92]
# datag=np.array([12,20,22,45])
# di = {
#     'a': 11,
#     'b': 22,
#     'c': 33,
#     'd': 44
# }

# hi= pd.Series(arr,di)
# print(hi)

series1 = pd.Series([1,2,3,4,5],index=['psl','ipl','bbl','ilt20','cpl'])

series2=pd.Series([1,2,3,6,5],index=['psl','ipl','bbl','BBB','cpl'] )


print(series1+series2)