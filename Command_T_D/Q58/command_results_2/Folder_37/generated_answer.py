import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(np.array(mat.reshape(-1, mat.shape[1]).T) == 64)
