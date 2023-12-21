
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    submatrices = []
    for sub_rows in range(1, rows+1):
        for sub_cols in range(1, cols+1):
            for i in range(rows+1-sub_rows):
                for j in range(cols+1-sub_cols):
                    submatrix = matrix[i:i+sub_rows, j:j+sub_cols]
                    if np.sum(submatrix) == 56:
                        submatrices.append(submatrix.tolist())
    return submatrices
