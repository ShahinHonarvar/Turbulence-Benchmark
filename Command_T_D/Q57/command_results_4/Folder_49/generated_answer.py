def submatrix_with_particular_sum(matrix):
    return [row[:] for row in matrix if row.sum() == -42]
