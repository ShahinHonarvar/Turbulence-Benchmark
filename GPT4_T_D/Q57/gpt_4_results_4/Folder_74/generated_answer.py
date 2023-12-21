
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    row, col = matrix.shape
    for sub_row in range(1, row+1):
        for sub_col in range(1, col+1):
            for i in range(row - sub_row + 1):
                for j in range(col - sub_col + 1):
                    sub_matrix = matrix[i: i + sub_row, j: j + sub_col]
                    if np.sum(sub_matrix) == 88:
                        result.append(sub_matrix)
    return result
