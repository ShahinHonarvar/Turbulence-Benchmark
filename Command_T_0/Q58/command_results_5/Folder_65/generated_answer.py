import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+35] == np.full(35, matrix[i]), axis=1) for i in range(len(matrix)-34) for j in range(i+1, len(matrix)))
