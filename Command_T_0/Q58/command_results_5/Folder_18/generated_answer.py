import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:j+104] == np.full(104, True), axis=1) for i in range(0, len(matrix)-103) for j in range(i+1, len(matrix)))
