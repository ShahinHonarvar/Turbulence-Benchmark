import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.where(np.all(matrix == 69, axis=1)), axis=0)
