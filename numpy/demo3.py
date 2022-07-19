import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1, 1:4])
print(arr2[0:2, 2])
print(arr2[0:2, 1:4])
print(arr.dtype)

arrs = np.array(["apple", "banana", "cherry"])
print(arrs.dtype)

arrs2 = np.array([1, 2, 3, 4], dtype='S')
print(arrs2)
print(arrs2.dtype)

arrs3 = np.array([1, 2, 3, 4], dtype='i4')
print(arrs3)
print(arrs3.dtype)