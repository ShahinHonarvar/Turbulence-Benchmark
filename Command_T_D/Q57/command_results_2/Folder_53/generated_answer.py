def submatrix_with_particular_sum(mat):
    return [[i for i in row if sum(row) == -37] for row in zip(*mat)]
