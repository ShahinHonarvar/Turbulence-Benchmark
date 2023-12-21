import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(matrix[row][:138] == 138 for row in range(len(matrix)))))
