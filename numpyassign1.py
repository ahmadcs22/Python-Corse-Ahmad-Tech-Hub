import numpy as np

# array = np.zeros(10)
# array = np.ones(10)
# array = np.ones(10)*5

# array = np.arange(10,51)
# array = np.arange(10,51,2)
# array=np.arange(0,9).reshape(3,3)
# array = np.eye(3,3)
# array=np.random.rand()
# array = np.random.randn(25)
# array = np.arange(1,101).reshape(10,10)/100
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]
array = np.arange(1,26).reshape(5,5)



# print(array[2:,1:])
# print(array[3,4])
# print(array[1:3,1:2])
# print(array[4])
# print(array[3:])
print(array.sum())
print(array.std())
print(array.sum(axis=0))