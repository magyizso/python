import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

for x in np.nditer(arr[:, ::2]):
    print(x)

for idx, x in np.ndenumerate(arr):
    print(idx, x)