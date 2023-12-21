
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_rows, n_cols = matrix.shape
    for i_start in range(n_rows):
        for i_end in range(i_start, n_rows):
            for j_start in range(n_cols):
                for j_end in range(j_start, n_cols):
                    submatrix = matrix[i_start:i_end+1, j_start:j_end+1]
                    if np.sum(submatrix) == -46:
                        submatrices.append(submatrix.tolist())
    return submatrices
