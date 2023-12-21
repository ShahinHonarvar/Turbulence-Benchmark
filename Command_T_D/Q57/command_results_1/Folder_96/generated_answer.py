def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            curr_sum = 0
            for curr_row in range(row, len(matrix)):
                curr_sum += matrix[curr_row][col]
            if curr_sum == -63:
                result += [[row, col]]
    return result
