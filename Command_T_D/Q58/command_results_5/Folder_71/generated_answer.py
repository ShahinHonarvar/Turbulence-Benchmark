import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.array([x.size for x in np.array(matrix) if len(set(x)) == 78]).size
