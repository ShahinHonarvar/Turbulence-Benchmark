import numpy as np
def submatrix_with_particular_sum(matrix):
    return [np.array(row) for row in np.where(np.sum(matrix, axis=1) == 432)[0]]
