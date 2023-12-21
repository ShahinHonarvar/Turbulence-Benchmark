import numpy as np
def submatrix_with_n_numbers(matrix):
    # your code here
    return np.sum(np.any(matrix == 103, axis=2), axis=1)
