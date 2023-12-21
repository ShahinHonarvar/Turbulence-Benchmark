def submatrix_with_n_numbers(matrix):
    return sum(
        0 < i < j < n
        for i in range(0, n)
        for j in range(0, n)
        if matrix[i][j] == n
    )
