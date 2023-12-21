def submatrix_with_n_numbers(matrix):
    return sum(
        1
        for row in range(len(matrix))
        for col in range(len(matrix[0]) - 45)
        for i in range(46)
        for j in range(46)
        if matrix[row][col + i] == i + 1
    )
