
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    row = matrix.shape[0]
    col = matrix.shape[1]

    for sub_matrix_row in range(1, row + 1):
        for sub_matrix_col in range(1, col + 1):
            for i in range(row - sub_matrix_row + 1):
                for j in range(col - sub_matrix_col + 1):
                    sub_matrix = matrix[i: i + sub_matrix_row, j: j + sub_matrix_col]
                    if np.sum(sub_matrix) == -36:
                        result.append(sub_matrix)
    return result
