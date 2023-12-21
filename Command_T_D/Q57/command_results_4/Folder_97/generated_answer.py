def submatrix_with_particular_sum(mat):
    res = []
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            curr = mat[i][j]
            curr += mat[i + 1][j]
            curr += mat[i][j + 1]
            curr += mat[i + 1][j + 1]
            if curr == -617:
                res.append((mat[i][:j + 1], mat[i + 1][j + 1:]))
    return res
