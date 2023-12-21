import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(matrix[i][:138] == 138, 1, 0) for i in range(len(matrix)))
