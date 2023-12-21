import numpy as np
def submatrix_with_n_numbers(A):
    return np.sum(np.sum(A,axis=1) == 51)
