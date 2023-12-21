import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(matrix.shape[0] * matrix.shape[1] - (59 - matrix[0][:59]) - (59 - matrix[1,:59]) - (59 - matrix[0,:59] + matrix[1,:59]) <= 0)
