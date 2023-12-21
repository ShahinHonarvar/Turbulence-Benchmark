
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for i in range(1, rows-r+1):
                for j in range(1, cols-c+1):
                    submatrix = matrix[r:r+i, c:c+j]
                    if submatrix.sum() == -57:
                        submatrices.append(submatrix.tolist())
    return submatrices
