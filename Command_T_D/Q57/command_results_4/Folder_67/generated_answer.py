def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(len(matrix)) for submatrix in range(len(matrix[row])) if matrix[row][submatrix] == 40]
