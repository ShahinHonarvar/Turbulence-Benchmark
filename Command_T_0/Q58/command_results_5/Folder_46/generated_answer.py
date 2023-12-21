import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+144] == matrix[i:j+144], axis=1) for i in range(0, len(matrix)-143) for j in range(i, len(matrix)-143))
