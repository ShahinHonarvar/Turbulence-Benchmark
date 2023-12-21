import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    matrix = matrix.reshape(len(matrix), len(matrix))
    return np.sum(np.equal(matrix, 131))
