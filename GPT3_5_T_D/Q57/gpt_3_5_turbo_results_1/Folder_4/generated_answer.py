
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(1, rows-i+1):
                for l in range(1, cols-j+1):
                    submatrix = matrix[i:i+k, j:j+l]
                    if np.sum(submatrix) == 87:
                        submatrices.append(submatrix.tolist())
    return submatrices
