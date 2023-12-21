def submatrix_with_particular_sum(matrix):
    return [list(submatrix) for submatrix in map(set, (m for m in matrix if sum(m) == -38)) if len(submatrix) > 1]
