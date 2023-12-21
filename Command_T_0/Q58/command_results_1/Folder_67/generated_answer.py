import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+43] == np.full(43, matrix[i]), axis=1) for i in range(0, len(matrix)-42) for j in range(i+1, len(matrix)))
