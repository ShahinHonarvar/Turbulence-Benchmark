def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(len(matrix)) for submatrix in range(len(matrix[0])) if sum(matrix[row][:submatrix] + matrix[row][submatrix+1:]) == 87]
