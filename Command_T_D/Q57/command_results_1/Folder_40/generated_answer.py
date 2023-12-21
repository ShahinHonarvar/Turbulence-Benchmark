def submatrix_with_particular_sum(matrix):
    return [
        (row, col)
        for row in range(len(matrix))
        for col in range(row, len(matrix))
        if sum(matrix[row][:col] + matrix[row][col + 1 :]) == -10
    ]
