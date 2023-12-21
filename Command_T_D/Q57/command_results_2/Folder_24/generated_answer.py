def submatrix_with_particular_sum(mat):
    return [list(submat) for i in range(len(mat)) for j in range(len(mat[0])) for submat in zip(mat[i], mat[i][j]) if len(set(submat)) == len(submat) and sum(submat) == -36]
