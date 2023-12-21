import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.hstack([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 53]))
