import numpy as np
def submatrix_with_particular_sum(arr):
    m = np.full((len(arr), len(arr)), 84, dtype=np.int32)
    for i in range(len(arr)):
        for j in range(len(arr)):
            m[i][j] = arr[i][j]
    return np.where(m == 84)
