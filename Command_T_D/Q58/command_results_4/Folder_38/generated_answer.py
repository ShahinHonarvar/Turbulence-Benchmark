def submatrix_with_n_numbers(matrix):
    return matrix.shape[0] * matrix.shape[1] * (matrix.shape[0] - 33) * (matrix.shape[1] - 33)
