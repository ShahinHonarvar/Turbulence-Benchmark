import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(np.sum(mat,axis=1)==103)
