
import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    all_submatrices, rows, cols = [], matrix.shape[0], matrix.shape[1]

    for row1 in range(rows):
        for col1 in range(cols):
            for row2 in range(row1, rows):
                for col2 in range(col1, cols):
                    submatrix = matrix[row1:row2+1, col1:col2+1]
                    if np.sum(submatrix) == 997:
                        all_submatrices.append(submatrix)
    return all_submatrices
