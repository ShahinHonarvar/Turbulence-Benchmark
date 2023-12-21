
import numpy as np

def submatrix_with_particular_sum(matrix):
    r, c = matrix.shape
    submatrix_list = []
    for row in range(r):
        for col in range(c):
            for s_row in range(row + 1, r + 1):
                for s_col in range(col + 1, c + 1):
                    submatrix = matrix[row: s_row, col: s_col]
                    if np.sum(submatrix) == 77:
                        submatrix_list.append(submatrix)
    return submatrix_list
