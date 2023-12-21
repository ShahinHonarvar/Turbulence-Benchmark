import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(np.stack([arr[i:j+1] for i in range(0, len(arr)-1)]), axis=1))
