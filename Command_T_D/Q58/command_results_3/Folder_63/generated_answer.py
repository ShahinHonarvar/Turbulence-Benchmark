import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.matrix(matrix)
    if len(matrix) < 57:
        return 0
    col_sum = [0] * len(matrix)
    for i in range(len(matrix[0])):
        col_sum[i] += matrix[0][i]
    matrix[0] = col_sum
    row_sum = [0] * len(matrix)
    for i in range(len(matrix[1])):
        row_sum[i] += matrix[1][i]
    matrix[1] = row_sum
    matrix[0][-1] += 1
    matrix[1][-1] += 1
    if matrix[0][-1] == 57:
        return 1
    else:
        return 0
