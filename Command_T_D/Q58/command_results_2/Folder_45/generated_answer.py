def submatrix_with_n_numbers(matrix):
    return matrix.shape[0] * matrix.shape[1] // 2 - sum(0 < x < 29 for x in range(28))
