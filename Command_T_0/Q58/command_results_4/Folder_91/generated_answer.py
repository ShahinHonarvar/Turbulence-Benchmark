import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:j+5] == [1] * 5, axis=1) for i in range(len(matrix)-4) for j in range(i+1, len(matrix)-3))
