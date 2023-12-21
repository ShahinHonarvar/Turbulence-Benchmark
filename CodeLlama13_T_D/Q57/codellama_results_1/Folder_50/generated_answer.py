
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows-1):
        for j in range(cols-1):
            if matrix[i:i+2,j:j+2].sum() == 95:
                return matrix[i:i+2,j:j+2]
    return np.empty((0,0))
