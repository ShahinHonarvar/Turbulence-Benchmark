def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row = matrix[i]
            col = matrix[0][j]
            if sum(row) == -261 and sum(col) == -261:
                res.append(matrix[i][:j] + matrix[i][j + 1:] + matrix[0][:j] + matrix[0][j + 1:])
    return res
