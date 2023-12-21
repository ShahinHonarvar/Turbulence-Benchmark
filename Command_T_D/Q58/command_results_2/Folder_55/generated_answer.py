import numpy as np
def submatrix_with_n_numbers(matrix):
    # Your code here
    return np.count_nonzero(np.sum(matrix, axis=0) == 39)
