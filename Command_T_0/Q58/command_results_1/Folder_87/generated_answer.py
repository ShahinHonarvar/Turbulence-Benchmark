import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+96] == matrix[i:j+96], axis=1) for i in range(0, len(matrix)-95) for j in range(i, len(matrix)-95))
