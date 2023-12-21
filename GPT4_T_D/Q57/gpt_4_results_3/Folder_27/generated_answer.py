
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices_that_sum_to_77 = []

    for row in range(rows):
        for col in range(cols):
            for submatrix_row in range(row+1, rows+1):
                for submatrix_col in range(col+1, cols+1):
                    submatrix = matrix[row:submatrix_row, col:submatrix_col]
                    if np.sum(submatrix) == 77:
                        submatrices_that_sum_to_77.append(submatrix)

    return submatrices_that_sum_to_77
