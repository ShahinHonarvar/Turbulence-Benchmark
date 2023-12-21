
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom+1, left:right+1]
                    if np.sum(submatrix) == 80:
                        submatrices.append(submatrix.tolist())
    return submatrices
