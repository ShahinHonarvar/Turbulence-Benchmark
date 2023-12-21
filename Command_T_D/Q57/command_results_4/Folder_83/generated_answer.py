def submatrix_with_particular_sum(mat):
    return [[k for k in row if k == -15] for row in zip(*mat)]
