def submatrix_with_particular_sum(matrix):
    matrix = [[x for x in range(77)] for _ in range(77)]
    for i in range(77):
        for j in range(77):
            matrix[i][j] = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
    return [[x for x in range(77)] for _ in range(77)]
