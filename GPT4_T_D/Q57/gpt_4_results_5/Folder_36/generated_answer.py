
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    submatrices = []
    for row_submatrix in range(1, rows + 1):
        for col_submatrix in range(1, cols + 1):
            for i in range(rows - row_submatrix + 1):
                for j in range(cols - col_submatrix + 1):
                    submatrix = matrix[i:i+row_submatrix, j:j+col_submatrix]
                    if np.sum(submatrix) == -779:
                        submatrices.append(submatrix)
    return submatrices
