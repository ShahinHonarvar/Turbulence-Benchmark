def submatrix_with_n_numbers(matrix):
    return sum(
        any(
            [
                True
                for i in range(n)
                for j in range(i + 1, n + 1)
                for k in range(j + 1, n + 1)
                for l in range(k + 1, n + 1)
            ]
        )
        for n in range(1, matrix.shape[0] + 1)
    )
