import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix == np.ones((27, 27))), axis=1)
