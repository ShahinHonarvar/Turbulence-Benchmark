import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(np.all(np.sum(np.all(mat == n, axis=1), axis=2) == 85 for n in range(1, 86)))
