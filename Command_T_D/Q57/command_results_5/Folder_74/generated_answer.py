import numpy as np
def submatrix_with_particular_sum(matrix):
    return [y for x in range(len(matrix)) for y in range(len(matrix[0])) if np.sum(matrix[x][y]) == 88]
