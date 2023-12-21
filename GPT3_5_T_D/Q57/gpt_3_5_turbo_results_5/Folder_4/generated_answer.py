
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(columns):
                for c_end in range(c_start, columns):
                    submatrix = matrix[r_start:r_end+1, c_start:c_end+1]
                    if np.sum(submatrix) == 87:
                        submatrices.append(submatrix)
    return submatrices
