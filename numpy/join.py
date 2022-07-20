import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newarr = np.concatenate((arr1, arr2))
print(newarr)

arr3 = np.array([[1,2,3], [4,5,6]])
arr4 = np.array([[7,8,9], [10,11,12]])

newarr2 = np.concatenate((arr3, arr4), axis=1)
print(newarr2)

newarr3 = np.stack((arr1, arr2), axis=1)
print(newarr3)

newarr4 = np.vstack((arr1, arr2))
print(newarr4)

newarr5 = np.hstack((arr1, arr2))
print(newarr5)

newarr6 = np.dstack((arr1, arr2))
print(newarr6)