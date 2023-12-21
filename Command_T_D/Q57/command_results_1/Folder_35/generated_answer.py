def submatrix_with_particular_sum(mat):
    return [mat[i:j] for i in range(0, len(mat)) for j in range(i, len(mat)) if sum(mat[i:j]) == 432]
