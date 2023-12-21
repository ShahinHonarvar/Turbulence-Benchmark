import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j, j:k] == 54, axis=1)) for i in range(len(matrix)-53) for j in range(53, len(matrix)) for k in range(53, j+1))
