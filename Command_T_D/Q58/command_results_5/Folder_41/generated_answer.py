import numpy as np
def submatrix_with_n_numbers(matrix):
    # Count the number of submatrices with n integers
    matrix = np.array(matrix)
    # Count the number of submatrices with n integers
    return np.sum(np.sum(matrix, axis=0) == 73)
