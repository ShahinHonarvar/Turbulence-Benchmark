
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for sub_row in range(1, rows+1):
        for sub_col in range(1, cols+1):
            for start_row in range(rows - sub_row + 1):
                for start_col in range(cols - sub_col + 1):
                    sub_matrix = matrix[start_row:(start_row + sub_row), start_col:(start_col + sub_col)]
                    if np.sum(sub_matrix) == 94:
                        result.append(sub_matrix)
    return result
