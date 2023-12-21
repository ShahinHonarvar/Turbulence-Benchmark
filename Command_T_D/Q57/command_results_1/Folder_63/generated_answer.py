def submatrix_with_particular_sum(mat):
    return [[sub] for row in mat for sub in zip(row, [64 - row[0]] * len(row))]
