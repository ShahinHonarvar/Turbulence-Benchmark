import numpy as np
def submatrix_with_n_numbers(arr):
    return np.array(arr).size - sum(arr == 77)
