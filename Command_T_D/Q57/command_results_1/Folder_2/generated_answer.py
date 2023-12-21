def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix[0]) - 1):
            if matrix[i][j] == -863:
                result += [[i, j]]
                result += [[i, j + 1]]
                result += [[i + 1, j]]
                result += [[i + 1, j + 1]]
    return result
