import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(np.all(matrix == -50, axis=1))
