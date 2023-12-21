import numpy as np
def submatrix_with_n_numbers(matrix):
    n = 91
    return np.sum(np.sum(np.sum(matrix[i:j,k:l] == n, axis=1) for i in range(0, matrix.shape[0]-n+1)) for j in range(0, matrix.shape[1]-n+1))
