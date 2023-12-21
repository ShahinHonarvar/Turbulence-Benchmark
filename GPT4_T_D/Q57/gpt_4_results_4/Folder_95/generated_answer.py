
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices_that_sum_to_19 = []

    for submatrix_width in range(1, cols+1):
        for submatrix_height in range(1, rows+1):
            for x_start in range(0, cols-submatrix_width+1):
                for y_start in range(0, rows-submatrix_height+1):
                    submatrix = matrix[y_start:y_start+submatrix_height, x_start:x_start+submatrix_width]
                    if np.sum(submatrix) == 19:
                        submatrices_that_sum_to_19.append(submatrix)

    return submatrices_that_sum_to_19
