
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for top_row in range(n):
        for left_col in range(m):
            for bottom_row in range(top_row + 1,n + 1):
                for right_col in range(left_col + 1, m + 1):
                    submatrix = matrix[top_row:bottom_row, left_col:right_col]
                    if np.sum(submatrix) == -77:
                        submatrices.append(submatrix)
    return submatrices
