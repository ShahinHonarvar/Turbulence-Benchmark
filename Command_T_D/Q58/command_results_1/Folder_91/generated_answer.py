import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.sum(matrix,axis=1)>4,axis=0))
