
import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_value = 752
    rows, cols = matrix.shape
    result = []

    for sub_row in range(rows):
        for sub_col in range(cols):
            for dim in range(1, min(rows-sub_row, cols-sub_col)+1):
                sub_mat = matrix[sub_row:sub_row+dim, sub_col:sub_col+dim]
                if np.sum(sub_mat) == sum_value:
                    result.append(sub_mat)

    return result
