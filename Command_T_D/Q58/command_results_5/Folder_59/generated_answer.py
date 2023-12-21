import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+77] == np.full(76, -1, dtype=np.int64), axis=1) for i in range(0, len(matrix) - 76) for j in range(i, i + 76))
