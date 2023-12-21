import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:j+7] == [1] * 7, axis=1) for i in range(len(matrix)-6) for j in range(i+1, len(matrix)-6))
