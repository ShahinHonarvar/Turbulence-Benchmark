def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            row = matrix[i]
            col = matrix[i][j]
            count = 0
            for k in range(j + 1, len(matrix[0])):
                count += matrix[i][k]
            for l in range(i + 1, len(matrix)):
                count += matrix[l]
            if count == 99:
                result.append((row, col, k, l))
    return result
