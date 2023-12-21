
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []
    for size in range(1, min(rows, columns) + 1):
        for x in range(0, rows - size + 1):
            for y in range(0, columns - size + 1):
                submatrix = matrix[x:x+size,y:y+size]
                if np.sum(submatrix) == -82:
                    submatrices.append(submatrix)
    return submatrices
