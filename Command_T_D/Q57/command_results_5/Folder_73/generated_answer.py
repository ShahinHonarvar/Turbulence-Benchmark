def submatrix_with_particular_sum(matrix):
    return [row for row in range(len(matrix)) if sum(matrix[row]) == 93]
