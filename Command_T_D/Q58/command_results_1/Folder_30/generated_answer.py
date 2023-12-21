import numpy as np
def submatrix_with_n_numbers(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    matrix = np.array(matrix)
    matrix = matrix.reshape(len(matrix), len(matrix[0]))
    return matrix.count(94)
