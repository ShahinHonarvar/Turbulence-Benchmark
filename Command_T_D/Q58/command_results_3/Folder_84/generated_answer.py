import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(matrix) // 127
