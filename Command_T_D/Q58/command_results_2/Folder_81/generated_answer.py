import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[start:start+97] == np.full(97, True), axis=1))
