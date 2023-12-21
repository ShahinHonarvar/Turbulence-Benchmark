
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for row_size in range(1, rows + 1):
        for col_size in range(1, cols + 1):
            for row in range(rows - row_size + 1):
                for col in range(cols - col_size + 1):
                    submatrix = matrix[row:row + row_size, col:col + col_size]
                    if np.sum(submatrix) == -3:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
