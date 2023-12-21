
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices_that_sum_to_zero = []

    for row1 in range(rows):
        for col1 in range(cols):
            for row2 in range(row1+1, rows+1):
                for col2 in range(col1+1, cols+1):
                    sub_matrix = matrix[row1:row2, col1:col2]
                    if np.sum(sub_matrix) == 0:
                        submatrices_that_sum_to_zero.append(sub_matrix)
    
    return submatrices_that_sum_to_zero
