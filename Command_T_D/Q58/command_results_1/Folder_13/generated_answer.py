import numpy as np
def submatrix_with_n_numbers(matrix):
    if len(matrix) < 175:
        return 0
    return sum(1 for i in range(len(matrix) - 174) if np.all(matrix[i:i + 175] == matrix[i + 175:]))
