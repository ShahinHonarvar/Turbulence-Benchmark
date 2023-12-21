import numpy as np
def submatrix_with_particular_sum(matrix):
    return [row for row in np.array(matrix) if np.sum(row) == -47]
