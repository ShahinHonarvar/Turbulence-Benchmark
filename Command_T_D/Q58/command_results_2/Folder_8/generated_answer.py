def submatrix_with_n_numbers(matrix):
    return matrix.shape[0] * matrix.shape[1] - sum(
        [0] * matrix.shape[0] for _ in range(matrix.shape[1])
    )
