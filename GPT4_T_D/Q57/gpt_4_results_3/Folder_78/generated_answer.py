
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = np.shape(mat)
    submatrices_of_sum_17 = []

    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix = mat[row:r+1, col:c+1]
                    if np.sum(submatrix) == 17:
                        submatrices_of_sum_17.append(submatrix.tolist())

    return submatrices_of_sum_17
