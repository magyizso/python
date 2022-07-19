import numpy as np

arr0 = np.array(42)
print(arr0)

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))

print(np.__version__)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('Number of dimensions of array:', arr.ndim)
print(arr3[-1, -1, -1])