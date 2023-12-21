import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(np.any(matrix[i:j+48] == 48 for i in range(0, len(matrix)-48) for j in range(i, len(matrix))))
