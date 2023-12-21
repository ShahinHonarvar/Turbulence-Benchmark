
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape

    for top in range(rows):
        for bottom in range(top + 1, rows + 1):
            for left in range(cols):
                for right in range(left + 1, cols + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if np.sum(submatrix) == 28:
                        submatrices.append(submatrix.tolist())

    return submatrices
