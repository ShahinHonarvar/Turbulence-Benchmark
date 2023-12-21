import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return sum(1 for row in range(len(matrix[0])) if np.sum(matrix[row] == 1, axis=1) == 72)
