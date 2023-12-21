
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    row, col = matrix.shape

    for row_index in range(row):
        for col_index in range(col):
            for row_len in range(row_index + 1, row + 1):
                for col_len in range(col_index + 1, col + 1):
                    submatrix = matrix[row_index:row_len, col_index:col_len]
                    if np.sum(submatrix) == 41:
                        submatrix_list.append(submatrix)
    return submatrix_list
