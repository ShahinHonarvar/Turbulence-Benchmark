def submatrix_with_particular_sum(mat):
    return [row[:] for row in mat if len(row) >= 3 and sum(row) == -452]
