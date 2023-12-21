import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.sum(arr[i][:122] == 122 for i in range(len(arr))), axis=0)
