
import numpy as np

def submatrix_with_particular_sum(matrix):
    row_end = len(matrix)
    col_end = len(matrix[0])
    result = []
    for row in range(row_end):
        for col in range(col_end):
            for r in range(row, row_end):
                for c in range(col, col_end):
                    sub_matrix = matrix[row:r+1, col:c+1]
                    if np.sum(sub_matrix) == 997:
                        result.append(sub_matrix.tolist())
    return result
