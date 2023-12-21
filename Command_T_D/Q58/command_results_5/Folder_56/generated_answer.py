import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    matrix = matrix[matrix.nonzero()]
    return len([sub for sub in matrix if len(set(sub)) == 68])
