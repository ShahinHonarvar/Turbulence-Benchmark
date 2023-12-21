import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.hstack((np.hstack((x == 115, x == 0)), (x == 115, x == 1)), (x == 115, x == 2)), (x == 115, x == 3)), axis=1)
