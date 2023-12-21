import numpy as np
def submatrix_with_n_numbers(matrix):
    # Your code here
    return np.sum(np.any(matrix, axis=1), axis=0) == 126
