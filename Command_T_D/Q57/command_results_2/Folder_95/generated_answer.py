def submatrix_with_particular_sum(mat):
    return [mat[i][j:] + mat[i + 1][j:] + mat[i][j + 1:] + mat[i + 1][j + 1:] for i in range(len(mat) - 1) for j in range(len(mat[0]) - 1)]
