import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(matrix[i:j+90] == 1, axis=1) == 90 for i in range(len(matrix) - 89) for j in range(i, len(matrix) - 90))
