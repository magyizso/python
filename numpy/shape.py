import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])

print(arr.shape)

arr = np.array([1,2,3,4], ndmin=5)

print(arr)
print('Shape of array: ', arr.shape)

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr1 = arr1.reshape(4,3)
newarr2 = arr1.reshape(2,3,2)
newarr3 = arr1.reshape(2,2,-1)

print(newarr1)
print(newarr2)
print(newarr2.base)
print(newarr3)

arr2 = np.array([[1,2,3], [4,5,6]])

newarr4 = arr2.reshape(-1)

print(newarr4)
