import numpy as np
def submatrix_with_n_numbers(matrix):
    # your code here
    return np.sum(np.sum(matrix == 1, axis=2) == 88)
