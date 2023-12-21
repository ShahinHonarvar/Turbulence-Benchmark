
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for r in range(row+1, rows+1):
                for c in range(col+1, cols+1):
                    submatrix = matrix[row:r, col:c]
                    if np.sum(submatrix) == 56:
                        submatrices.append(submatrix)
    return submatrices
