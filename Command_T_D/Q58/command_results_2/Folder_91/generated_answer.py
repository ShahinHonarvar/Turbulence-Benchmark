import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(arr[i:j+5] == np.full(5, arr[i:j+5]), axis=1) for i in range(0, len(arr)-4) for j in range(i+1, len(arr)-3))
