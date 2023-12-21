import numpy as np
def submatrix_with_n_numbers(matrix):
    if len(matrix) == 0:
        return 0
    if len(matrix) == 1:
        return 0
    if len(matrix) == 2:
        return 0
    return np.sum( np.sum(np.sum(0 <= matrix[0][:176]),axis=1),axis=0 )
