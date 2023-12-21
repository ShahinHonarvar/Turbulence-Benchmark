import numpy as np
def submatrix_with_particular_sum(matrix):
    return [row for row in np.array(matrix).reshape(-1, len(matrix[0])).T if np.sum(row) == 411]
