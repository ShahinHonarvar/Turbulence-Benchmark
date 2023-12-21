def submatrix_with_particular_sum(matrix):
    return [row[row.index(row[0]) + 1:]+[row[0]] for row in matrix] if matrix.shape[0] >= 2 else []
