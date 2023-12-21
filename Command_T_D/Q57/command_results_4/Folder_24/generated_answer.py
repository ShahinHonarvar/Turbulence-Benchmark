import numpy as np
def submatrix_with_particular_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    return np.where(np.all(np.sum(matrix[i:j+1, :], axis=1) == -36, axis=0) for i in range(m) for j in range(i, n))
