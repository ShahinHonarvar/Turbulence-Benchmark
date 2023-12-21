import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum( mat.shape[0] >= 130 and mat.shape[1] >= 130 )
