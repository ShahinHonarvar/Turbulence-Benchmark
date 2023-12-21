import numpy as np
def submatrix_with_n_numbers(mat):
    return np.count_nonzero(np.all(np.hstack(np.all(mat == i, axis=1) for i in range(1, 14)), axis=0), axis=0)
