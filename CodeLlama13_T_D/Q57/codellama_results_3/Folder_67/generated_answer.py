
def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 40:
                return [[matrix[i][j]]]
            else:
                for k in range(i + 1, rows):
                    for l in range(j + 1, cols):
                        if matrix[k][l] == 40 - (matrix[i][j] + matrix[k][l]):
                            return [[matrix[i][j]] + [matrix[k][l]]]
    return []
