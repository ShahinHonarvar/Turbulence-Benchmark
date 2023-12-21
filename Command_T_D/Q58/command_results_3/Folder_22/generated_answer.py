import numpy as np
def submatrix_with_n_numbers(A):
    return sum(sum(np.unique(X)) == 21 for X in np.where(A)[0])
