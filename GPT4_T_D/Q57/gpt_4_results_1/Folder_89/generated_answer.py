
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrix_list = []
    for submatrix_height in range(1, m+1):
        for submatrix_width in range(1, n+1):
            for start_row in range(m-submatrix_height+1):
                for start_col in range(n-submatrix_width+1):
                    end_row = start_row + submatrix_height
                    end_col = start_col + submatrix_width
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if np.sum(submatrix) == 80:
                        submatrix_list.append(submatrix)
    return submatrix_list
