
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r_start in range(rows):
        for r_end in range(r_start+1, rows+1):
            for c_start in range(cols):
                for c_end in range(c_start+1, cols+1):
                    submatrix = matrix[r_start:r_end, c_start:c_end]
                    if np.sum(submatrix) == -87:
                        submatrices.append(submatrix.tolist())
    return submatrices
