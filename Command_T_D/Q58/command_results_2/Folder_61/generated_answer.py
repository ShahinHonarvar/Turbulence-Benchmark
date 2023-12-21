import numpy as np
def submatrix_with_n_numbers(matrix):
    #find all submatrices of size 4x4
    #one way to do this is to find all submatrices of size 2x2
    #and then find all submatrices of size 4x4
    return np.count_nonzero(np.sum(matrix,axis=0)>3)
