def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = 3
            row_sum = 0
            col_sum = 0
            for row in range(row, len(matrix)):
                row_sum += matrix[row][col]
            for col in range(col, len(matrix[0])):
                col_sum += matrix[row][col]
            if row_sum == col_sum == 3:
                result += [[row, col]]
    return result
