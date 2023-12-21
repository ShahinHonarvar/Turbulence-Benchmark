def submatrix_with_particular_sum(matrix):
    return [submatrix for submatrix in matrix.split() if sum(submatrix) == 15]
