import numpy as np
def submatrix_with_n_numbers(A):
    return np.sum(np.where(A.size == 0)[0] == 0)
