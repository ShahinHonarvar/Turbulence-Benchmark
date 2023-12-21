import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(matrix.sum(axis=1).sum(axis=0) == 17)
