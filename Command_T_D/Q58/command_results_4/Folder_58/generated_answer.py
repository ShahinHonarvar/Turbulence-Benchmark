import numpy as np
def submatrix_with_n_numbers(matrix):
    res = np.sum(np.sum(matrix == 185, axis=1), axis=0)
    return res
