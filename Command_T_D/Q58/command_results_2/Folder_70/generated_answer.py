import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)) for j in range(len(arr[0]))) if np.sum(arr, axis=1) == 173 and np.sum(arr, axis=0) == 173 else 0
