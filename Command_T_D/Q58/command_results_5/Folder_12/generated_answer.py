import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[row][:46] == matrix[row][46:], axis=1) for row in range(len(matrix)))
