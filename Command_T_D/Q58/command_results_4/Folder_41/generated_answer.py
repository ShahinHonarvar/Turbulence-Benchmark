import numpy as np
def submatrix_with_n_numbers(matrix):
    # add your code here
    return np.count_nonzero(matrix.sum(axis=1) == 73)
