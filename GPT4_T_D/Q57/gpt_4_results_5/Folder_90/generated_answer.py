
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows = matrix.shape[0]
    cols = matrix.shape[1]

    for row in range(rows):
        for col in range(cols):
            for width in range(1, cols-col+1):
                for height in range(1, rows-row+1):
                    submatrix = matrix[row:row+height, col:col+width]
                    if np.sum(submatrix) == -452:
                        submatrices.append(submatrix)

    return submatrices
