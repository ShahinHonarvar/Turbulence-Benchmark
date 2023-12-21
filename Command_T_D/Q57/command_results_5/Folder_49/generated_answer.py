def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == -42:
                res += [[matrix[i][:j + 1], matrix[i + 1][:j + 1], matrix[i][j + 1:], matrix[i + 1][j + 1:]]
    return res
