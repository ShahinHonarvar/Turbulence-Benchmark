import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for submatrix in matrix.tolist() if np.sum(submatrix) == -25]
