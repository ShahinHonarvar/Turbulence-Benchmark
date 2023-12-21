def submatrix_with_n_numbers(matrix):
    return sum(
        (
            True
            if matrix[i][j] == 92 and matrix[i][k] == 92 and matrix[k][j] == 92 and matrix[k][k] == 92
            else False
        )
        for i in range(len(matrix))
        for j in range(len(matrix[0]))
        for k in range(len(matrix[0]))
    )
