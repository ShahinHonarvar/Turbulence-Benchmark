import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[row][:144] == np.sum(matrix[row][:144]), axis=1) for row in range(len(matrix)))
