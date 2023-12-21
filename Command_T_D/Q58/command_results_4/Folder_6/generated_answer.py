import numpy as np
def submatrix_with_n_numbers(np_matrix):
    return np.sum(np.sum(np_matrix == 122, axis=1) == np.shape(np_matrix)[1])
