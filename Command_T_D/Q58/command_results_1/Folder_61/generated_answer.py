def submatrix_with_n_numbers(matrix):
    return sum(
        sum(
            1
            for row in range(0, matrix.shape[0])
            for col in range(0, matrix.shape[1])
            if matrix[row][col] == 1
        )
        == 4
    )
