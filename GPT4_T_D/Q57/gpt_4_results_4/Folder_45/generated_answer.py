
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for sub_row_size in range(1, rows-row+1):
                for sub_col_size in range(1, cols-col+1):
                    submatrix = matrix[row:row+sub_row_size, col:col+sub_col_size]
                    if np.sum(submatrix) == -77:
                        submatrices.append(submatrix.tolist())
    return submatrices
