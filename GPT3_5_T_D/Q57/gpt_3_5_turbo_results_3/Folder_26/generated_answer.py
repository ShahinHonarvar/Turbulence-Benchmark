
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape

    for r in range(rows):
        for c in range(cols):
            for i in range(r + 1, rows + 1):
                for j in range(c + 1, cols + 1):
                    submatrix = matrix[r:i, c:j]
                    if np.sum(submatrix) == 997:
                        submatrices.append(submatrix.tolist())

    return submatrices
