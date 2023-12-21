
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for a in range(x+1, rows+1):
                for b in range(y+1, cols+1):
                    submatrix = matrix[x:a, y:b]
                    if np.sum(submatrix) == -15:
                        submatrices.append(submatrix)
    return submatrices
