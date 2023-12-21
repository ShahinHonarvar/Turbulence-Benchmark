def submatrix_with_particular_sum(mat):
    return [row[:] for row in mat if row.sum() == -157]
