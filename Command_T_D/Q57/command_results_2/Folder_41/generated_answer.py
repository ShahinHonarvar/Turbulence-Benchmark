def submatrix_with_particular_sum(matrix):
    return [submatrix for submatrix in matrix.tolist() if sum(submatrix) == -26]
