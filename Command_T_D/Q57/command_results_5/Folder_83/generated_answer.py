def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(len(matrix)) for submatrix in zip(matrix[row], [matrix[row][:], matrix[row][1:], matrix[row][:1], matrix[row][1:1]]) if sum(submatrix) == -15]
