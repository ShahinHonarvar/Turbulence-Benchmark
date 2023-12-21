import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:j, j:k] == 8, axis=1) for i in range(len(matrix)) for j in range(i, len(matrix)) for k in range(j, len(matrix)))
