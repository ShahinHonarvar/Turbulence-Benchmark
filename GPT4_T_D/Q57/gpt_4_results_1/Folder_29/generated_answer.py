
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for row_dim in range(1, rows + 1):
        for col_dim in range(1, cols + 1):
            for i in range(rows - row_dim + 1):
                for j in range(cols - col_dim + 1):
                    submatrix = matrix[i:i+row_dim,j:j+col_dim]
                    if np.sum(submatrix) == 84:
                        submatrices.append(submatrix)

    return submatrices
