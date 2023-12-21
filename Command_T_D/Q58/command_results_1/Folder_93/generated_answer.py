def submatrix_with_n_numbers(matrix):
    return matrix.shape[0] * matrix.shape[1] - sum(sum(row) == 53 for row in matrix)
