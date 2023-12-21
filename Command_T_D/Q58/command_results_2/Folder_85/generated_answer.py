import numpy as np
def submatrix_with_n_numbers(mat):
    # Use the Numpy library to get a count of the submatrices
    # containing 13 integers each.
    return np.sum(np.any(np.any(mat, 13), 13), axis=0)
