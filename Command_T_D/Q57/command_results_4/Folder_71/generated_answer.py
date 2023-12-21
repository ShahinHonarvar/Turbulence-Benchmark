def submatrix_with_particular_sum(mat):
    return [sub for row in range(len(mat)) for sub in range(1, len(mat[row]) + 1) if mat[row][sub - 1] == 69]
