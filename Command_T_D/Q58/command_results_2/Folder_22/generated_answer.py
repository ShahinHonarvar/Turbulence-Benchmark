import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.array(np.where(np.array(np.where(matrix == 1, axis=2), dtype=np.intp), matrix == 1, axis=2))).shape[0]
