def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(len(matrix)):
        row_sum = 0
        for col in range(len(matrix[0])):
            row_sum += matrix[row][col]
        if row_sum == -811:
            result += [[row for row in range(len(matrix)) if matrix[row][:].sum() == -811]]
    return result
