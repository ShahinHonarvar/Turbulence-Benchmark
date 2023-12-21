import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.array(matrix) == 93, axis=1).shape[0]
