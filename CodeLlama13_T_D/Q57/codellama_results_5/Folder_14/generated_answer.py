
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:, j:]
            if np.allclose(np.sum(submatrix), -93):
                return list(submatrix)
    return []
