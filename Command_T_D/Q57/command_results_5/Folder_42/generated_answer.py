def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(matrix.shape[0]) for submatrix in range(matrix.shape[1]) if matrix[row][submatrix] == 862]
