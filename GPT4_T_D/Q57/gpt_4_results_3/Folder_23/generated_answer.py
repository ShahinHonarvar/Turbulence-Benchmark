
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for m in range(r+1, rows+1):
                for n in range(c+1, cols+1):
                    submatrix = matrix[r:m, c:n]
                    if np.sum(submatrix) == 59:
                        submatrices.append(submatrix)
    return submatrices
