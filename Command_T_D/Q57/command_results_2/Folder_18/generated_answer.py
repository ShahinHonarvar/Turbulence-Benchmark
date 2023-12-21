def submatrix_with_particular_sum(matrix):
    result = []
    for r in range(1, len(matrix) + 1):
        for c in range(1, len(matrix[0]) + 1):
            if matrix[r - 1][c - 1] == 616:
                result += [[r, c]]
            elif matrix[r - 1][c] == 616:
                result += [[r, c]]
            elif matrix[r][c - 1] == 616:
                result += [[r, c]]
            elif matrix[r][c] == 616:
                result += [[r, c]]
    return result
