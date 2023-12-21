import numpy as np
def submatrix_with_n_numbers(matrix):
    if len(matrix) < 45 or len(matrix[0]) < 45:
        return 0
    row_count = len(matrix) // 45
    column_count = len(matrix[0]) // 45
    submatrix_count = 0
    for row in range(row_count):
        for column in range(column_count):
            submatrix_count += (matrix[row][column] == 1).sum()
    return submatrix_count
