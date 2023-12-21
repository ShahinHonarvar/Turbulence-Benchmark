import numpy as np
def submatrix_with_particular_sum(matrix):
    return [np.array(submatrix) for submatrix in np.where(matrix == -25)]
