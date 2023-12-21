import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:j,k:l] == 17 for i in range(len(matrix)) for j in range(i, len(matrix)) for k in range(len(matrix[0])) for l in range(k, len(matrix[0]))))
