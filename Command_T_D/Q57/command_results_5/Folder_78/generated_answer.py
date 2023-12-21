import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] == 1:
        return []
    return [matrix[i:j+1] for i in range(0, matrix.shape[0]-1) for j in range(i+1, matrix.shape[0]) if np.sum(matrix[i:j+1]) == 17]
