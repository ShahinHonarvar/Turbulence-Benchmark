def submatrix_with_particular_sum(matrix):
    return [matrix[i][:j] for i in range(len(matrix)) for j in range(i, len(matrix)) if matrix[i][j] == -308]
