
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    submatrices = []
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            for i in range(rows - sub_rows + 1):
                for j in range(cols - sub_cols + 1):
                    submatrix = matrix[i:i+sub_rows, j:j+sub_cols]
                    if np.sum(submatrix) == 66:
                        submatrices.append(submatrix)
    return submatrices
