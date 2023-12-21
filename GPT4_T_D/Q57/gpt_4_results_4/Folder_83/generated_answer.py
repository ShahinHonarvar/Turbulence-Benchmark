
import numpy as np

def submatrix_with_particular_sum(m):
    rows, cols = m.shape
    submatrices = []

    for row1 in range(rows):
        for col1 in range(cols):
            for row2 in range(row1, rows):
                for col2 in range(col1, cols):
                    submatrix = m[row1:row2+1, col1:col2+1]
                    if np.sum(submatrix) == -15:
                        submatrices.append(submatrix)

    return submatrices
