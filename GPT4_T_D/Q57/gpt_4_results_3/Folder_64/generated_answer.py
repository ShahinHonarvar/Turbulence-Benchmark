
import numpy as np

def submatrix_with_particular_sum(matrix):
    found_sub_matrices = []
    row_length = len(matrix)
    col_length = len(matrix[0]) if matrix else 0

    for row_start in range(row_length):
        for row_end in range(row_start+1, row_length+1):
            for col_start in range(col_length):
                for col_end in range(col_start+1, col_length+1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(submatrix) == -4:
                        found_sub_matrices.append(submatrix)
    return found_sub_matrices
