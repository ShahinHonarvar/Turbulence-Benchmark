import numpy as np
def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            row_sum = 0
            col_sum = 0
            for r in range(row, matrix.shape[0]):
                for c in range(col, matrix.shape[1]):
                    row_sum += matrix[r][c]
                    col_sum += matrix[row][c]
            if row_sum == -255 and col_sum == -255:
                result.append(matrix[row][:])
    return result
