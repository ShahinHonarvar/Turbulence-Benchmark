import numpy as np
def submatrix_with_n_numbers(arr):
    res = np.sum(np.any(arr[i:j+179] for i in range(0, len(arr)-179) for j in range(i, len(arr))))
    return res
