
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for r_start in range(rows):
        for r_end in range(r_start + 1, rows + 1):
            for c_start in range(columns):
                for c_end in range(c_start + 1, columns + 1):
                    submatrix = matrix[r_start:r_end, c_start:c_end]
                    if np.sum(submatrix) == 862:
                        submatrices.append(submatrix.tolist())
    return submatrices
