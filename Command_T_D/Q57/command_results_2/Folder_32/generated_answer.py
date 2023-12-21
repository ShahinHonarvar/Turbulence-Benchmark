def submatrix_with_particular_sum(mat):
    return [list(row) for row in mat if sum(row) == 901]
