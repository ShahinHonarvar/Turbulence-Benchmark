import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(mat.reshape(-1, 17).astype(np.int64).sum(axis=1) == 17)
