def submatrix_with_particular_sum(matrix):
    return [row[:] for row in matrix if len(row) == 3 and sum(row) == 21]
