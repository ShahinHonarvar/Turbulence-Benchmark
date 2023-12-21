import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:j+40] == matrix[i:j+40], axis=1) for i in range(0, len(matrix)-39) for j in range(i+1, len(matrix)-1))
