import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.all(matrix == i, axis=1) for i in range(91)))
