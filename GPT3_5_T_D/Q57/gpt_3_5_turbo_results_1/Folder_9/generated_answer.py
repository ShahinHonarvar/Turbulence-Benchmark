
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    submatrix = matrix[r:i+1, c:j+1]
                    if np.sum(submatrix) == -86:
                        submatrices.append(submatrix)
    return submatrices
