def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == -394:
                if matrix[i - 1][j] == -394:
                    result.append(([row[j] for row in matrix[:i]] + [[row[j + 1] for row in matrix[i + 1 :]]))
                if matrix[i + 1][j] == -394:
                    result.append(([row[j] for row in matrix[:i]] + [[row[j + 1] for row in matrix[i + 1 :]]))
                if matrix[i - 1][j - 1] == -394:
                    result.append(([row[j - 1] for row in matrix[:i]] + [[row[j + 1] for row in matrix[i + 1 :]]))
                if matrix[i + 1][j - 1] == -394:
                    result.append(([row[j - 1] for row in matrix[:i]] + [[row[j + 1] for row in matrix[i + 1 :]]))
    return result
