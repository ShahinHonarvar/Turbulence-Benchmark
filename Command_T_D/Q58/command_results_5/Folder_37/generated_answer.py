def submatrix_with_n_numbers(matrix):
    return sum(
        1
        for i in range(len(matrix) - 63)
        for j in range(len(matrix[0]) - 63)
        for k in range(len(matrix) - i - 63)
        for l in range(len(matrix[0]) - j - 63)
        if all(
            matrix[i][j] == matrix[k][l]
            for k in range(i, i + 63)
            for l in range(j, j + 63)
        )
    )
