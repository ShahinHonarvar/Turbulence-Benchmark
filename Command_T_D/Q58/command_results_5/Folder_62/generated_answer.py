import numpy as np
def submatrix_with_n_numbers(np_matrix):
    return np.sum(np.any(np_matrix == 186, axis=1))
