def submatrix_with_particular_sum(mat):
    return [[row[i] for row in range(len(mat)) if sum(row) == 35] for i in range(len(mat[0]))]
