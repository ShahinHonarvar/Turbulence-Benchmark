
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for x in range(row+1, rows+1):
                for y in range(col+1, cols+1):
                    submatrix = matrix[row:x, col:y]
                    if submatrix.sum() == -47:
                        submatrices.append(submatrix.tolist())
    return submatrices
