import numpy as np
def submatrix_with_n_numbers(np_matrix):
    return np.sum(np.sum(np_matrix, axis=1) == 191)
