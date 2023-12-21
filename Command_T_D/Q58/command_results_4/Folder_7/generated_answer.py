def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix) - 1):
        for col in range(row, len(matrix[0]) - 1):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
                continue
            count += matrix[row][col]
            if count == 121:
                matrix[row][col] = 0
                count = 0
    return count
