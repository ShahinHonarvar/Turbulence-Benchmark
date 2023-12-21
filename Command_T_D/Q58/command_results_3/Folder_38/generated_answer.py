def submatrix_with_n_numbers(matrix):
    return matrix.shape[0] * matrix.shape[1] // 2 * (matrix.shape[0] - 1) * (matrix.shape[1] - 1) // 9 * 2
