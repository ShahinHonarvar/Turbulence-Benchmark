import numpy as np
def submatrix_with_n_numbers(mat):
    return np.count_nonzero(np.logical_and(np.all(np.sum(mat,axis=1)==56,axis=1),np.all(np.sum(mat,axis=0)==56,axis=0)))
