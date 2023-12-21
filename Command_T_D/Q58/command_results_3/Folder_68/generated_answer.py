import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(arr[i:j+1, j:k+1] == np.full(k+1, 74, np.int32), axis=0) for i in range(0, len(arr)-74) for j in range(0, len(arr)-74))
