import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+92] == np.full(92, matrix[i]), axis=1) for i in range(0, len(matrix)-91) for j in range(i+1, len(matrix)))
