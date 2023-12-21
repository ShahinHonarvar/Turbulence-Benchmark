
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape

    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(columns):
                for c2 in range(c1 + 1, columns + 1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if np.sum(submatrix) == -37:
                        submatrices.append(submatrix.tolist())

    return submatrices
