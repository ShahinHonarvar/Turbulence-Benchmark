
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sum_needed = -617
    result = []
    for top_row in range(rows):
        for left_col in range(cols):
            for bot_row in range(top_row, rows):
                for right_col in range(left_col, cols):
                    sub_mat = matrix[top_row:bot_row+1, left_col:right_col+1]
                    if np.sum(sub_mat) == sum_needed:
                        result.append(sub_mat)

    return result
