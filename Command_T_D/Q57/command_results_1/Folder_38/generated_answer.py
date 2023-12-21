import numpy as np
def submatrix_with_particular_sum(matrix):
    return [row for row in np.where(np.sum(matrix, axis=1) == 34)[0]]
