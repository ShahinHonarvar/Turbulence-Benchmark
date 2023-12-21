
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_with_sum_21 = []
    rows, cols = matrix.shape
    for submatrix_width in range(1, cols+1):
        for submatrix_height in range(1, rows+1):
            for start_col in range(0, cols-submatrix_width+1):
                for start_row in range(0, rows-submatrix_height+1):
                    submatrix = matrix[start_row:start_row+submatrix_height, start_col:start_col+submatrix_width]
                    if np.sum(submatrix) == 21:
                        submatrices_with_sum_21.append(submatrix)
    return submatrices_with_sum_21
