def submatrix_with_particular_sum(mat):
    return [submatrix for row in range(len(mat)) for col in range(len(mat[0])) for submatrix in range(row, row + col + 1)]
