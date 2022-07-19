import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr1 = np.array([1, 0, 3, 2])

newarr1 = arr1.astype('bool')
print(newarr1)
print(newarr1.dtype)