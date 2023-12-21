def submatrix_with_particular_sum(mat):
    res = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            tmp = mat[i][j]
            cnt = 1
            for k in range(j, len(mat[0]) - 1):
                if mat[i][k] != -57:
                    tmp += mat[i][k]
                    cnt += 1
                else:
                    break
            if tmp == -57:
                res += [[tmp] * cnt]
    return res
